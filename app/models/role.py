from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models.role_permission import RolePermission
from app.models.link_tables import UserRoleLink, RolePermissionLink
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.permission import Permission 

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None

    users: List["User"] = Relationship(back_populates="roles", link_model=UserRoleLink)
    permissions: List["Permission"] = Relationship(back_populates="roles", link_model=RolePermissionLink)

