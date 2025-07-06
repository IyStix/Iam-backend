from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from app.models.role import Role
from app.models.relations import UserRole 
from app.models.link_tables import UserRoleLink
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.role import Role

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    hashed_password: str

    roles: List["Role"] = Relationship(back_populates="users", link_model=UserRoleLink)
