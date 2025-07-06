from sqlmodel import create_engine, Session, SQLModel
import os
from app.models.relations import UserRole
from app.models.role_permission import RolePermission


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    from app.models.user import User
    from app.models.role import Role
    from app.models.permission import Permission
    from app.models.relations import UserRole
    from app.models.role_permission import RolePermission
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
