from typing import Optional
from sqlmodel import SQLModel

class PermissionCreate(SQLModel):
    name: str
    description: Optional[str] = None

class PermissionRead(SQLModel):
    id: int
    name: str
    description: Optional[str]

class PermissionUpdate(SQLModel):
    name: Optional[str] = None
