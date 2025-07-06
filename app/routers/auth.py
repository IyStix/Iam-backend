from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from jose import jwt
from app.db import get_db


from app.core.ldap import ldap_authenticate
from app.core.security import SECRET_KEY, ALGORITHM
from app.services.user_service import get_user_by_username
from app.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = form_data.username
    password = form_data.password

    # LDAP first
    if ldap_authenticate(username, password):
        roles = ["admin"]
    else:
        # Local DB fallback
        user = get_user_by_username(db, username)
        if not user or user.hashed_password != password:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        roles = [role.name for role in user.roles]

    payload = {
        "sub": username,
        "roles": roles,
        "exp": datetime.utcnow() + timedelta(minutes=60)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

