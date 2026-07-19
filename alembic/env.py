"""Async Alembic environment for infrastructure-only schema evolution."""

import asyncio
import logging
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import AsyncEngine, async_engine_from_config

from alembic import context
from backend.composition.settings import get_settings
from backend.infrastructure.database.base import Base

# Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata from declarative base
target_metadata = Base.metadata

logger = logging.getLogger("alembic.env")


def run_migrations_offline() -> None:
    """Run migrations without creating a database connection."""
    logger.info("Starting offline database migrations.")
    url = get_settings().database_url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Configure and execute migrations using an async connection bridge."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Create the engine from environment configuration and run migrations."""
    logger.info("Starting online database migrations.")
    settings = get_settings()
    
    # Configure engine options for Alembic
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = settings.database_url
    
    # Create async engine with settings
    connectable: AsyncEngine = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        echo=settings.db_echo,
    )
    
    # Run migrations
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    
    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations against the configured asynchronous database."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
