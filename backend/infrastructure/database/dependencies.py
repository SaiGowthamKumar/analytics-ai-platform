"""Explicit FastAPI database dependency adapters."""

from collections.abc import AsyncIterator
from typing import cast

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from backend.composition.container import ApplicationContainer


async def get_db_session(request: Request) -> AsyncIterator[AsyncSession]:
    """Yield a session from the explicitly composed database infrastructure."""
    container = cast(ApplicationContainer, request.app.state.container)
    async with container.database.session() as session:
        yield session
