"""Technical bootstrap health contract tests."""

from fastapi.testclient import TestClient

from backend.composition.bootstrap import app


def test_health_reports_liveness_and_correlation_id() -> None:
    """The bootstrap exposes a safe, correlation-aware health response."""
    client = TestClient(app)

    response = client.get("/api/v1/health", headers={"X-Correlation-ID": "health-test-1"})

    assert response.status_code == 200
    assert response.headers["X-Correlation-ID"] == "health-test-1"
    assert response.json() == {
        "status": "ok",
        "service": "ai-analytics-platform",
        "version": "0.1.0",
        "correlation_id": "health-test-1",
    }
