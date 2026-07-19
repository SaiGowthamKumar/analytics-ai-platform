"""Initial empty migration for data platform infrastructure.

Revision ID: 0001_initial_empty
Revises:
Create Date: 2026-07-18
"""

from collections.abc import Sequence

revision: str = "0001_initial_empty"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Create no tables; this establishes the migration baseline."""


def downgrade() -> None:
    """Revert no tables; this establishes the migration baseline."""
