from sqlmodel import Session, select
from app.models.role import Role

def get_roles(session: Session):
    return session.exec(select(Role)).all()

def get_role(session: Session, role_id: int):
    return session.get(Role, role_id)

def create_role(session: Session, role: Role):
    session.add(role)
    session.commit()
    session.refresh(role)
    return role
