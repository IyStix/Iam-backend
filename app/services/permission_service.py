from sqlmodel import Session, select
from app.models.permission import Permission

def get_permissions(session: Session):
    return session.exec(select(Permission)).all()

def get_permission(session: Session, perm_id: int):
    return session.get(Permission, perm_id)

def create_permission(session: Session, permission: Permission):
    session.add(permission)
    session.commit()
    session.refresh(permission)
    return permission
