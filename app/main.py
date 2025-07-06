from app.db import Base, engine
from fastapi import FastAPI
from app.core.db import init_db
from app.routers import users, roles, permissions, auth

app = FastAPI(title="IAM Backend – EPITA")

@app.on_event("startup")
def on_startup():
    init_db()

# Routes principales
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(roles.router, prefix="/roles", tags=["Roles"])
app.include_router(permissions.router, prefix="/permissions", tags=["Permissions"])

Base.metadata.create_all(bind=engine)
