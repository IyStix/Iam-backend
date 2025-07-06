from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.core.security import SECRET_KEY, ALGORITHM, oauth2_scheme
from app.core.ldap import ldap_authenticate
from jose import jwt

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not ldap_authenticate(form_data.username, form_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = jwt.encode({
        "sub": form_data.username,
        "roles": ["admin"],  # Temporaire. À extraire dynamiquement depuis LDAP si besoin
        "exp": timedelta(minutes=60).total_seconds()
    }, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}
