from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    """Test the basic health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "Weather VibeCheck API"}
