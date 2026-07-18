"""Technical HTTP delivery components for bootstrap-only endpoints."""

import re
from typing import Any, cast
from uuid import uuid4

from fastapi import APIRouter, FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from backend.composition.container import ApplicationContainer
from backend.shared.correlation import correlation_id

_CORRELATION_ID_HEADER = "X-Correlation-ID"
_CORRELATION_ID_PATTERN = re.compile(r"^[A-Za-z0-9._-]{1,128}$")


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """Attach a validated correlation identifier to each HTTP exchange."""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Create or accept a safe identifier and propagate it to the response."""
        supplied_id = request.headers.get(_CORRELATION_ID_HEADER, "")
        request_id = supplied_id if _CORRELATION_ID_PATTERN.fullmatch(supplied_id) else str(uuid4())
        token = correlation_id.set(request_id)
        request.state.correlation_id = request_id

        try:
            response = await call_next(request)
        finally:
            correlation_id.reset(token)

        response.headers[_CORRELATION_ID_HEADER] = request_id
        return response


class HealthResponse(BaseModel):
    """Safe liveness response for orchestration and diagnostics."""

    status: str
    service: str
    version: str
    correlation_id: str


def _container(request: Request) -> ApplicationContainer:
    """Read the composed container without creating hidden dependencies."""
    return cast(ApplicationContainer, request.app.state.container)


def _error_body(request: Request, code: str, message: str, details: Any = None) -> dict[str, Any]:
    """Build the public error envelope without exposing internal state."""
    return {
        "error": {"code": code, "message": message, "details": details},
        "correlationId": getattr(request.state, "correlation_id", ""),
    }


router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
def get_health(request: Request) -> HealthResponse:
    """Report process liveness without checking unconfigured dependencies."""
    container = _container(request)
    return HealthResponse(
        status="ok",
        service=container.settings.service_name,
        version=container.settings.service_version,
        correlation_id=request.state.correlation_id,
    )


def register_exception_handlers(application: FastAPI) -> None:
    """Register global transport error translation during bootstrap."""

    @application.exception_handler(RequestValidationError)
    async def handle_validation_error(
        request: Request,
        exception: RequestValidationError,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=_error_body(
                request, "INVALID_REQUEST", "Request validation failed.", exception.errors()
            ),
        )

    @application.exception_handler(StarletteHTTPException)
    async def handle_http_error(
        request: Request,
        exception: StarletteHTTPException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=exception.status_code,
            content=_error_body(request, "HTTP_ERROR", str(exception.detail)),
        )

    @application.exception_handler(Exception)
    async def handle_unexpected_error(request: Request, exception: Exception) -> JSONResponse:
        _container(request).logger.exception("Unhandled request exception")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=_error_body(request, "INTERNAL_ERROR", "An unexpected error occurred."),
        )
