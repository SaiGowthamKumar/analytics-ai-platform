"""FastAPI application factory and lifespan composition root."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.composition.container import ApplicationContainer
from backend.composition.http import (
    CorrelationIdMiddleware,
    api_router,
    register_exception_handlers,
    root_router,
)
from backend.composition.settings import get_settings
from backend.shared.logging import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Reserve lifecycle management without registering business resources."""
    yield


def create_application() -> FastAPI:
    """Create the technical backend foundation without business modules."""
    settings = get_settings()
    logger = configure_logging(settings.log_level)
    container = ApplicationContainer(settings=settings, logger=logger)

    application = FastAPI(
        title=settings.service_name,
        version=settings.service_version,
        lifespan=lifespan,
        docs_url="/docs" if settings.docs_enabled else None,
        redoc_url=None,
        openapi_url="/openapi.json" if settings.docs_enabled else None,
    )
    application.state.container = container
    application.add_middleware(CorrelationIdMiddleware)
    application.include_router(root_router)
    application.include_router(api_router, prefix=settings.api_prefix)
    register_exception_handlers(application)
    return application


app = create_application()
