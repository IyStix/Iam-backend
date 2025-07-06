import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def new_user_data():
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "hashed_password": "secret123"
    }

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user(new_user_data):
    response = client.post("/users/", json=new_user_data)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["username"] == new_user_data["username"]
    assert data["email"] == new_user_data["email"]
    # Note: normalement, le password ne doit pas être retourné

def test_update_user(new_user_data):
    # Crée un user d'abord (ou prends un user existant)
    create_resp = client.post("/users/", json=new_user_data)
    user_id = create_resp.json()["id"]

    update_data = {
        "username": "updateduser",
        "email": "updated@example.com",
        "hashed_password": "newsecret"
    }
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "updateduser"
    assert data["email"] == "updated@example.com"

def test_delete_user(new_user_data):
    # Crée un user d'abord
    create_resp = client.post("/users/", json=new_user_data)
    user_id = create_resp.json()["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200 or response.status_code == 204

    # Vérifie qu’il n’existe plus
    get_resp = client.get(f"/users/{user_id}")
    assert get_resp.status_code == 405
