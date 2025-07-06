# IAM - Identity and Access Management

Frontend + Backend pour un système de gestion des utilisateurs, rôles, permissions, et authentification via LDAP ou fallback DB. Projet académique EPITA 2025.

---

## 🧱 Stack

- **Backend**: FastAPI, SQLModel, PostgreSQL
- **Frontend**: React + Vite + TailwindCSS
- **Auth**: LDAP (fallback DB)
- **ORM**: SQLModel (basé sur SQLAlchemy)
- **DB**: PostgreSQL

---

## 🖥️ Installation

```bash
git clone <repo>
cd iam-backend
python3.11 -m venv iam-env
source iam-env/bin/activate
pip install -r requirements.txt
make run (pour lancer le serveur)
cp .env.example .env


### Lancer le front

cd iam-frontend
npm install
npm run dev


### Liens

swagger: http://localhost:8000/docs
frontend: http://localhost:5173/ , http://localhost:5173/users , http://localhost:5173/roles , http://localhost:5173/permissions
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
