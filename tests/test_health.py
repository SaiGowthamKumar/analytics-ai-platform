"""Health endpoint tests for the technical backend foundation."""

from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from backend.composition.bootstrap import app


@pytest.mark.parametrize("path", ["/health", "/live"])
def test_process_health_endpoints_report_liveness(path: str) -> None:
    """Every process-only endpoint returns the standard health response."""
    client = TestClient(app)

    response = client.get(path, headers={"X-Correlation-ID": "health-test-1"})

    assert response.status_code == 200
    assert response.headers["X-Correlation-ID"] == "health-test-1"
    assert response.json() == {
        "status": "ok",
        "service": "ai-analytics-platform",
        "version": "0.1.0",
        "correlationId": "health-test-1",
    }


def test_readiness_reports_healthy_database() -> None:
    """Readiness is available when the injected database probe succeeds."""
    client = TestClient(app)
    database = app.state.container.database
    database.is_healthy = AsyncMock(return_value=True)

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_readiness_reports_unavailable_database() -> None:
    """Readiness fails safely when the database probe cannot connect."""
    client = TestClient(app)
    database = app.state.container.database
    database.is_healthy = AsyncMock(return_value=False)

    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json()["error"]["code"] == "DATABASE_UNAVAILABLE"
