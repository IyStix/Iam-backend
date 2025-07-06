from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user_schema import UserUpdate
from sqlalchemy import select
from app.models.user import User
from app.models.user import User


def get_users(session: Session):
    return session.exec(select(User)).all()

def get_user(session: Session, user_id: int):
    return session.get(User, user_id)

def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(session: Session, user_id: int) -> dict:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"detail": "User deleted successfully"}

def update_user(session: Session, user_id: int, user_update: UserUpdate) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = user_update.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user_by_username(db, username: str):
    stmt = select(User).where(User.username == username)
    result = db.execute(stmt)
    return result.scalars().first()
