import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def new_role_data():
    return {
        "name": "testrole",
    }

def test_list_roles():
    response = client.get("/roles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_role(new_role_data):
    response = client.post("/roles/", json=new_role_data)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["name"] == new_role_data["name"]

def test_update_role(new_role_data):
    create_resp = client.post("/roles/", json=new_role_data)
    role_id = create_resp.json()["id"]

    update_data = {
        "name": "updatedrole",
    }
    response = client.put(f"/roles/{role_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "updatedrole"

def test_delete_role(new_role_data):
    create_resp = client.post("/roles/", json=new_role_data)
    role_id = create_resp.json()["id"]

    response = client.delete(f"/roles/{role_id}")
    assert response.status_code in (200, 204)

    get_resp = client.get(f"/roles/{role_id}")
    assert get_resp.status_code == 405
