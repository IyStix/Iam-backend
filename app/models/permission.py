from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models.role_permission import RolePermission

if TYPE_CHECKING:
    from app.models.role import Role

class Permission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None  # <- Ajout nécessaire ici

    roles: List["Role"] = Relationship(back_populates="permissions", link_model=RolePermission)
