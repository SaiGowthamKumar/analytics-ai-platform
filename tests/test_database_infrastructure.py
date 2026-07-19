"""Infrastructure-only database session factory tests."""

import asyncio

from backend.composition.settings import Settings
from backend.infrastructure.database.connection import Database


def test_database_exposes_async_session_factory() -> None:
    """Creating a session does not require a connection or a business model."""
    settings = Settings(
        database_url="postgresql+asyncpg://test_user:test_password@localhost:5432/test_database"
    )
    database = Database(settings)

    session = database.session_factory()

    asyncio.run(session.close())
    asyncio.run(database.dispose())
