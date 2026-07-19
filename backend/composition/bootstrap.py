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
from backend.infrastructure.database.connection import Database
from backend.shared.logging import configure_logging


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncIterator[None]:
    """Dispose technical infrastructure during application shutdown."""
    try:
        yield
    finally:
        container: ApplicationContainer = application.state.container
        await container.database.dispose()


def create_application() -> FastAPI:
    """Create the technical backend foundation without business modules."""
    settings = get_settings()
    logger = configure_logging(settings.log_level)
    database = Database(settings)
    container = ApplicationContainer(settings=settings, logger=logger, database=database)

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
    
    # Log startup information
    logger.info("Database initialized", extra={
        "pool_size": settings.db_pool_size,
        "max_overflow": settings.db_max_overflow,
        "pool_timeout": settings.db_pool_timeout,
        "pool_recycle": settings.db_pool_recycle,
        "echo": settings.db_echo
    })
    
    return application


app = create_application()
