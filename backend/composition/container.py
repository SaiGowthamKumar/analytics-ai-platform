"""Explicit technical composition without hidden instantiation."""

import logging

from backend.composition.settings import Settings
from backend.infrastructure.database.connection import Database


class ApplicationContainer:
    """Hold explicit infrastructure dependencies in a transparent composition root."""

    def __init__(
        self,
        settings: Settings,
        logger: logging.Logger,
        database: Database,
    ) -> None:
        """Accept fully-initialized infrastructure components."""
        self.settings = settings
        self.logger = logger
        self.database = database
