"""Technical HTTP delivery configuration for bootstrap endpoints only."""

import re
from typing import Any, cast
from uuid import uuid4

from fastapi import APIRouter, FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from backend.composition.container import ApplicationContainer
from backend.shared.correlation import correlation_id

_CORRELATION_ID_HEADER = "X-Correlation-ID"
_CORRELATION_ID_PATTERN = re.compile(r"^[A-Za-z0-9._-]{1,128}$")


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """Propagate a validated correlation ID through each request."""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Accept a safe ID or generate one, then attach it to the response."""
        incoming_id = request.headers.get(_CORRELATION_ID_HEADER, "")
        request_id = incoming_id if _CORRELATION_ID_PATTERN.fullmatch(incoming_id) else str(uuid4())
        token = correlation_id.set(request_id)
        request.state.correlation_id = request_id
        try:
            response = await call_next(request)
        finally:
            correlation_id.reset(token)
        response.headers[_CORRELATION_ID_HEADER] = request_id
        return response


class HealthResponse(BaseModel):
    """Process-only health response."""

    status: str
    service: str
    version: str
    correlation_id: str = Field(serialization_alias="correlationId")


class ErrorDetail(BaseModel):
    """Consistent public error detail."""

    code: str
    message: str
    details: Any = None


class ErrorResponse(BaseModel):
    """Consistent public error envelope."""

    error: ErrorDetail
    correlation_id: str = Field(serialization_alias="correlationId")


def _container(request: Request) -> ApplicationContainer:
    """Retrieve the explicitly composed technical dependencies."""
    return cast(ApplicationContainer, request.app.state.container)


def _error_response(
    request: Request,
    http_status: int,
    code: str,
    message: str,
    details: Any = None,
) -> JSONResponse:
    """Translate technical failures into the consistent safe response model."""
    response = ErrorResponse(
        error=ErrorDetail(code=code, message=message, details=details),
        correlation_id=getattr(request.state, "correlation_id", ""),
    )
    return JSONResponse(status_code=http_status, content=response.model_dump(by_alias=True))


health_router = APIRouter(tags=["health"])
api_router = APIRouter()
root_router = APIRouter()


@health_router.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
@health_router.get("/ready", response_model=HealthResponse, status_code=status.HTTP_200_OK)
@health_router.get("/live", response_model=HealthResponse, status_code=status.HTTP_200_OK)
def get_process_health(request: Request) -> HealthResponse:
    """Return process health without invoking external dependencies."""
    settings = _container(request).settings
    return HealthResponse(
        status="ok",
        service=settings.service_name,
        version=settings.service_version,
        correlation_id=request.state.correlation_id,
    )


root_router.include_router(health_router)


def register_exception_handlers(application: FastAPI) -> None:
    """Register global technical exception translation."""

    @application.exception_handler(RequestValidationError)
    async def handle_validation_error(
        request: Request,
        exception: RequestValidationError,
    ) -> JSONResponse:
        return _error_response(
            request,
            status.HTTP_400_BAD_REQUEST,
            "INVALID_REQUEST",
            "Request validation failed.",
            exception.errors(),
        )

    @application.exception_handler(StarletteHTTPException)
    async def handle_http_exception(
        request: Request,
        exception: StarletteHTTPException,
    ) -> JSONResponse:
        return _error_response(request, exception.status_code, "HTTP_ERROR", str(exception.detail))

    @application.exception_handler(Exception)
    async def handle_unexpected_exception(request: Request, exception: Exception) -> JSONResponse:
        _container(request).logger.exception("Unhandled request exception")
        return _error_response(
            request,
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "INTERNAL_ERROR",
            "An unexpected error occurred.",
        )
