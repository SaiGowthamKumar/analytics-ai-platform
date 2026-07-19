"""Declarative base reserved for future infrastructure-owned ORM mappings."""

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# Define standard naming convention for database constraints
naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    """Shared declarative base; no ORM models are defined in this PR."""

    metadata = MetaData(naming_convention=naming_convention)
