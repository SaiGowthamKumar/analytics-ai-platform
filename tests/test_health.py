"""Health endpoint tests for the technical backend foundation."""

import pytest
from backend.composition.bootstrap import app
from fastapi.testclient import TestClient


@pytest.mark.parametrize("path", ["/health", "/ready", "/live"])
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
