# 🔐 IAM Backend – EPITA

Projet complet de gestion des identités (IAM) avec :
- Authentification via LDAP
- JWT + OAuth2
- RBAC avec rôles et permissions
- API FastAPI + Swagger
- PostgreSQL
- Dockerisé et prêt pour CI

## Installation

```bash
git clone <repo>
cd iam-backend
make setup
make run
```

## Routes

- POST /auth/login
- GET /users/
- CRUD /roles, /permissions

## Test

```bash
make test
```

## Docs

Swagger: http://localhost:8000/docs
