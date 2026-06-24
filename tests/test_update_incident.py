from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_update_incident():

    create = client.post(
        "/items",
        json = {
            "short_description": "Original",
            "description": "Original desc",
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

    update = client.put(
        f"/items/{incident['incident_id']}",
        json = {
            "status": "resolved"
        }
    )
    

    assert update.status_code == 200

    updated = update.json()

    ##print("\nUPDATE:")
    ##print(update.json())

    assert ( updated["status"] == "resolved")