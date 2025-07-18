from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db import get_session
from app.schemas.role_schema import RoleCreate, RoleRead
from app.models.role import Role
from app.services import role_service

router = APIRouter()

@router.get("/", response_model=list[RoleRead])
def list_roles(session: Session = Depends(get_session)):
    return role_service.get_roles(session)

@router.post("/", response_model=RoleRead)
def create_role(role: RoleCreate, session: Session = Depends(get_session)):
    db_role = Role.from_orm(role)
    return role_service.create_role(session, db_role)

@router.put("/{role_id}", response_model=RoleRead)
def update_role(role_id: int, role: RoleCreate, session: Session = Depends(get_session)):
    return role_service.update_role(session, role_id, role)

@router.delete("/{role_id}")
def delete_role(role_id: int, session: Session = Depends(get_session)):
    return role_service.delete_role(session, role_id)
