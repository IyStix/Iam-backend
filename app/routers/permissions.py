from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.schemas.permission_schema import PermissionCreate, PermissionRead
from app.models.permission import Permission
from app.services import permission_service

router = APIRouter()

@router.get("/", response_model=list[PermissionRead])
def list_permissions(session: Session = Depends(get_session)):
    return permission_service.get_permissions(session)

@router.post("/", response_model=PermissionRead)
def create_permission(permission: PermissionCreate, session: Session = Depends(get_session)):
    db_permission = Permission.from_orm(permission)
    return permission_service.create_permission(session, db_permission)

@router.put("/{permission_id}", response_model=PermissionRead)
def update_permission(permission_id: int, permission: PermissionCreate, session: Session = Depends(get_session)):
    return permission_service.update_permission(session, permission_id, permission)

@router.delete("/{permission_id}")
def delete_permission(permission_id: int, session: Session = Depends(get_session)):
    return permission_service.delete_permission(session, permission_id)
