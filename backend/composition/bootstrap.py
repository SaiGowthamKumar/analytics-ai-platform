"""Application bootstrap and explicit technical dependency wiring."""

from fastapi import FastAPI

from backend.composition.container import ApplicationContainer
from backend.composition.http import CorrelationIdMiddleware, register_exception_handlers, router
from backend.composition.settings import get_settings
from backend.shared.logging import configure_logging


def create_application() -> FastAPI:
    """Create the FastAPI delivery application without business modules."""
    settings = get_settings()
    logger = configure_logging(settings.log_level)
    container = ApplicationContainer(settings=settings, logger=logger)

    application = FastAPI(
        title=settings.service_name,
        version=settings.service_version,
        docs_url="/docs" if settings.docs_enabled else None,
        redoc_url=None,
        openapi_url="/openapi.json" if settings.docs_enabled else None,
    )
    application.state.container = container
    application.add_middleware(CorrelationIdMiddleware)
    application.include_router(router, prefix=settings.api_prefix)
    register_exception_handlers(application)
    return application


app = create_application()
