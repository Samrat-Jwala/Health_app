from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_route():
    """Test the root endpoint using FastAPI's TestClient."""
    response = client.get("/")

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json() == {"message": "Welcome to the Health Checkup API"}