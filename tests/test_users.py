from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    res = client.post("/auth/login", data={"username": "abdel", "password": "test123"})
    return res.json()["access_token"]

def test_get_users_authenticated():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    res = client.get("/users/", headers=headers)
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_users_unauthorized():
    res = client.get("/users/")
    assert res.status_code == 401

def test_get_users_unauthenticated():
    response = client.get("/users/")
    assert response.status_code == 401  # Unauthorized

def test_get_users_invalid_token():
    headers = {"Authorization": "Bearer invalid.token.value"}
    response = client.get("/users/", headers=headers)
    assert response.status_code == 401  # Unauthorized