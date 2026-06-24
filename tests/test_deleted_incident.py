from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_deleted_incident():

    create = client.post(
        "/items",
        json={
            "short_description": "Delete test",
            "description": "Delete me",
            "criticality": "high",
            "status": "open",
            "reporter": "test-user",
            "assigned_to": "backend",
            "service_name": "incident-api",
            "environment": "production"
        }
    )
    ##print("\nCREATE:")
    ##print(create.json())

    incident = create.json()

    delete = client.delete(f"/items/{incident['incident_id']}")
    
    ##print("DELETE:")
    ##print(delete.json())

    assert delete.status_code == 200

    verify = client.get(f"/items/{incident['incident_id']}")

    ##print("VERIFY:")
    ##print(verify.status_code)
    
    assert verify.status_code == 404