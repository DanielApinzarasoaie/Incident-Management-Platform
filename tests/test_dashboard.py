from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

def test_dashboard():
    
    response = client.get("/items/dashboard")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data,dict)

    assert "Total incidents" in data
    
    assert "Open incidents" in data

    assert "Resolved incidents" in data

    assert "In progress incidents" in data

    assert "On hold incidents" in data

    assert "Critical incidents" in data

    assert "High incidents" in data

    assert "Medium incidents" in data

    assert "Low incidents" in data

    assert "Production incidents" in data

    assert "Integration incidents" in data

    assert "Development incidents" in data

    assert "Assigned incidents" in data


    assert "Unassigned incidents" in data

