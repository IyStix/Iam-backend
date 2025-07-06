import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def new_permission_data():
    return {"name": "create_users"}

def test_create_permission(new_permission_data):
    response = client.post("/permissions/", json=new_permission_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == new_permission_data["name"]
    assert "id" in data

def test_list_permissions():
    response = client.get("/permissions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_permission(new_permission_data):
    # Créer d'abord une permission
    create_resp = client.post("/permissions/", json=new_permission_data)
    permission_id = create_resp.json()["id"]

    updated_data = {"name": "update_users"}
    update_resp = client.put(f"/permissions/{permission_id}", json=updated_data)
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "update_users"

def test_delete_permission(new_permission_data):
    # Créer d'abord une permission
    create_resp = client.post("/permissions/", json=new_permission_data)
    permission_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/permissions/{permission_id}")
    assert delete_resp.status_code == 200

    # Vérifier qu'elle n'existe plus
    list_resp = client.get("/permissions/")
    permissions = list_resp.json()
    assert all(p["id"] != permission_id for p in permissions)
