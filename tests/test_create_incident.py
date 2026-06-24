from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_incident():
    payload = {
        "short_description": "API failure",
        "description": "Service unavailable",
        "criticality": "high",
        "status": "open",
        "reporter": "test-user",
        "assigned_to": "backend",
        "service_name": "incident-api",
        "environment": "production"
    }

    response = client.post("/items",json=payload)
    
    assert response.status_code ==200

    data = response.json()

    assert data["incident_id"].startswith("INC")