"""Centralized structured logging configuration."""

import json
import logging
from datetime import UTC, datetime
from logging import LogRecord

from backend.shared.correlation import correlation_id


class JsonFormatter(logging.Formatter):
    """Emit safe, structured, correlation-aware application logs."""

    def format(self, record: LogRecord) -> str:
        """Serialize a log record without request bodies or secrets."""
        return json.dumps(
            {
                "timestamp": datetime.now(UTC).isoformat(),
                "level": record.levelname,
                "logger": record.name,
                "message": record.getMessage(),
                "correlation_id": correlation_id.get() or None,
            },
            default=str,
        )


def configure_logging(log_level: str) -> logging.Logger:
    """Configure and return the reusable application logger."""
    logger = logging.getLogger("ai_analytics_platform")
    logger.setLevel(log_level.upper())
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)

    return logger
