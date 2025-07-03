from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/auth/login", data={"username": "abdel", "password": "test123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_failure():
    response = client.post("/auth/login", data={"username": "abdel", "password": "wrong"})
    assert response.status_code == 401

def test_login_wrong_username():
    response = client.post("/auth/login", data={"username": "wrong", "password": "test123"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

def test_login_wrong_password():
    response = client.post("/auth/login", data={"username": "abdel", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

def test_login_missing_fields():
    response = client.post("/auth/login", data={"username": "abdel"})
    assert response.status_code == 422  # Unprocessable Entity

def test_token_structure():
    response = client.post("/auth/login", data={"username": "abdel", "password": "test123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert len(data["access_token"].split(".")) == 3  # JWT format: header.payload.signature