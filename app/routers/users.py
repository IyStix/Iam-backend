from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db import get_session
from app.schemas.user_schema import UserCreate, UserRead
from app.models.user import User
from app.services import user_service
from app.core.audit import log_action

router = APIRouter()

@router.get("/", response_model=list[UserRead])
def list_users(session: Session = Depends(get_session)):
    return user_service.get_users(session)

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = User.from_orm(user)
    log_action('create_user', user.username)
    return user_service.create_user(session, db_user)
