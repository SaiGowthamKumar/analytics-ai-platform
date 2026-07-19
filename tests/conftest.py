"""Technical bootstrap test configuration."""

import os

os.environ.setdefault(
    "APP_DATABASE_URL",
    "postgresql+asyncpg://test_user:test_password@localhost:5432/test_database",
)
