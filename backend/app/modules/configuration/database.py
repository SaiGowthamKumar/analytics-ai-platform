"""Database configuration and session management."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from backend.composition.settings import Settings
from backend.infrastructure.database.connection import Database


def create_database(settings: Settings) -> Database:
    """Create database instance with settings."""
    return Database(settings)


def get_session_factory(database: Database) -> async_sessionmaker[AsyncSession]:
    """Get session factory from database instance."""
    return database.session_factory


@asynccontextmanager
async def get_db_session(database: Database) -> AsyncIterator[AsyncSession]:
    """Provide a database session as a context manager."""
    async with database.session() as session:
        yield session