"""Explicit dependency wiring for technical bootstrap concerns."""

from dataclasses import dataclass
from logging import Logger

from backend.composition.settings import Settings


@dataclass(frozen=True, slots=True)
class ApplicationContainer:
    """Technical dependencies injected into delivery components."""

    settings: Settings
    logger: Logger
