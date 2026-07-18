"""Explicit technical dependency container."""

from dataclasses import dataclass
from logging import Logger

from backend.composition.settings import Settings


@dataclass(frozen=True, slots=True)
class ApplicationContainer:
    """Dependencies available to technical delivery adapters."""

    settings: Settings
    logger: Logger
