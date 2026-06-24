from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_get_missing_incident():

    response = client.get("/items/INC999999")

    assert response.status_code == 404

    assert "not found" in ( response.json()["detail"].lower())