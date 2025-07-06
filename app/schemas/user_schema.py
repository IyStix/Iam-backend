from typing import Optional
from sqlmodel import SQLModel

class UserCreate(SQLModel):
    username: str
    email: str
    hashed_password: str

class UserRead(SQLModel):
    id: int
    username: str
    email: str

class UserUpdate(SQLModel):
    username: Optional[str]
    email: Optional[str]
    hashed_password: Optional[str]
