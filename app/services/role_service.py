from sqlmodel import Session, select
from app.models.role import Role
from app.schemas.role_schema import RoleUpdate

def get_roles(session: Session):
    return session.exec(select(Role)).all()

def get_role(session: Session, role_id: int):
    return session.get(Role, role_id)

def create_role(session: Session, role: Role):
    session.add(role)
    session.commit()
    session.refresh(role)
    return role

def update_role(db: Session, role_id: int, role_update: RoleUpdate):
    db_role = get_role(db, role_id)
    if not db_role:
        return None
    for key, value in role_update.dict(exclude_unset=True).items():
        setattr(db_role, key, value)
    db.commit()
    db.refresh(db_role)
    return db_role

def delete_role(db: Session, role_id: int):
    db_role = get_role(db, role_id)
    if not db_role:
        return None
    db.delete(db_role)
    db.commit()
    return db_role
