from typing import Optional
from sqlmodel import SQLModel

class RoleCreate(SQLModel):
    name: str

class RoleRead(SQLModel):
    id: int
    name: str

class RoleUpdate(SQLModel):
    name: Optional[str] = None
