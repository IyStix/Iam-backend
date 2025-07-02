from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token
from datetime import timedelta

router = APIRouter()

# Faux utilisateur LDAP simulé
fake_users = {
    "abdel": {
        "username": "abdel",
        "password": "test123",  # En prod => hashé !
        "roles": ["admin"]
    }
}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": user["username"], "roles": user["roles"]},
        expires_delta=timedelta(minutes=60)
    )
    return {"access_token": access_token, "token_type": "bearer"}
