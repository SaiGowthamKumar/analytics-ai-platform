"""Safe structured logging for the technical bootstrap."""

import json
import logging
from datetime import UTC, datetime
from logging import LogRecord

from backend.shared.correlation import correlation_id


class JsonFormatter(logging.Formatter):
    """Format records as structured JSON without request content."""

    def format(self, record: LogRecord) -> str:
        """Produce a safe, correlation-aware log payload."""
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
    """Configure the application logger once during composition."""
    logger = logging.getLogger("ai_analytics_platform")
    logger.setLevel(log_level.upper())
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)

    return logger
