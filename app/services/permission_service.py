from sqlmodel import Session, select
from app.models.permission import Permission
from app.schemas.permission_schema import PermissionUpdate

def get_permissions(session: Session):
    return session.exec(select(Permission)).all()

def get_permission(session: Session, perm_id: int):
    return session.get(Permission, perm_id)

def create_permission(session: Session, permission: Permission):
    session.add(permission)
    session.commit()
    session.refresh(permission)
    return permission

def update_permission(db: Session, permission_id: int, permission_update: PermissionUpdate):
    db_permission = get_permission(db, permission_id)
    if not db_permission:
        return None
    for key, value in permission_update.dict(exclude_unset=True).items():
        setattr(db_permission, key, value)
    db.commit()
    db.refresh(db_permission)
    return db_permission

def delete_permission(db: Session, permission_id: int):
    db_permission = get_permission(db, permission_id)
    if not db_permission:
        return None
    db.delete(db_permission)
    db.commit()
    return db_permission
