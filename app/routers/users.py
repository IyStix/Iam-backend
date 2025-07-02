from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter()

@router.get("/")
def list_users(token: str = Depends(oauth2_scheme)):
    # Simule une liste d'utilisateurs
    return [{"id": 1, "username": "abdel"}, {"id": 2, "username": "test"}]
