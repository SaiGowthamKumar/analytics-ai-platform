"""FastAPI dependencies for database session management."""

from collections.abc import AsyncIterator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.composition.container import ApplicationContainer
from backend.infrastructure.database.connection import Database


async def get_database(container: ApplicationContainer = Depends()) -> Database:  # noqa: B008
    """Get database instance from container."""
    return container.database


async def get_db_session(
    database: Database = Depends(get_database),  # noqa: B008
) -> AsyncIterator[AsyncSession]:
    """Provide a database session dependency."""
    async with database.session() as session:
        yield session