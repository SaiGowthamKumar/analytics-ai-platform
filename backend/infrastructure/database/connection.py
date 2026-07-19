"""Asynchronous SQLAlchemy engine and session infrastructure."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

from sqlalchemy import text
from sqlalchemy.engine import make_url
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from backend.composition.settings import Settings

logger = logging.getLogger(__name__)


class Database:
    """Own the technical database engine and reusable async session factory."""

    def __init__(self, settings: Settings) -> None:
        """Create infrastructure without connecting until it is used."""
        # Fail-fast validation of database URL before engine creation
        if not settings.database_url or not settings.database_url.strip():
            raise ValueError(
                "Database configuration error: database_url must be configured and cannot be empty."
            )

        # Parse URL to safely log connection intent without exposing credentials
        try:
            parsed_url = make_url(settings.database_url)
            safe_url = parsed_url.render_as_string(hide_password=True)
        except Exception:
            safe_url = "invalid-database-url"

        logger.info(
            "Initializing database engine",
            extra={
                "database_url": safe_url,
                "pool_size": settings.db_pool_size,
                "max_overflow": settings.db_max_overflow,
                "pool_timeout": settings.db_pool_timeout,
                "pool_recycle": settings.db_pool_recycle,
                "echo": settings.db_echo,
            },
        )

        # Configure engine options based on settings
        engine_options: dict[str, Any] = {
            "pool_pre_ping": True,
            "pool_size": settings.db_pool_size,
            "max_overflow": settings.db_max_overflow,
            "pool_timeout": settings.db_pool_timeout,
            "pool_recycle": settings.db_pool_recycle,
            "echo": settings.db_echo,
        }

        self._engine: AsyncEngine = create_async_engine(
            settings.database_url,
            **engine_options,
        )
        self._session_factory = async_sessionmaker(self._engine, expire_on_commit=False)

    @property
    def session_factory(self) -> async_sessionmaker[AsyncSession]:
        """Expose the reusable factory without hiding dependencies."""
        return self._session_factory

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        """Provide an async session with deterministic cleanup and logging on failure."""
        try:
            session = self._session_factory()
        except Exception as e:
            logger.error("Failed to instantiate database session from factory", exc_info=e)
            raise

        try:
            async with session:
                yield session
        except Exception as e:
            logger.error("Database session encountered error during context execution", exc_info=e)
            raise

    async def is_healthy(self) -> bool:
        """Perform a minimal connectivity probe with SELECT 1 and log status."""
        try:
            async with self._engine.connect() as connection:
                await connection.execute(text("SELECT 1"))
            logger.info("Database connectivity check succeeded.")
            return True
        except SQLAlchemyError as e:
            logger.error("Database connectivity check failed", exc_info=e)
            return False

    async def dispose(self) -> None:
        """Release pool resources during application shutdown."""
        logger.info("Disposing database engine pool.")
        await self._engine.dispose()
