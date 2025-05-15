import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_appointment():
    """Test creating an appointment using FastAPI's TestClient"""
    payload = {
        "user_id": 1,
        "reason": "General checkup"
    }

    response = client.post("/appointments/", json=payload)

    assert response.status_code in {200, 201}, f"Unexpected status code: {response.status_code}"
    assert "id" in response.json(), "Response JSON missing 'id' field"