# 🔐 IAM Backend – EPITA

Backend du projet **Identity & Access Management** développé dans le cadre du projet EPITA.

Permet :
- Authentification avec JWT
- Gestion des utilisateurs (simulée)
- Gestion des rôles (simulée)
- Intégration future LDAP/AD et RBAC
- API documentée avec Swagger

---

## ⚙️ Prérequis

- Python 3.10+ (idéalement via [pyenv](https://github.com/pyenv/pyenv))
- Git (pour cloner le repo)

---

## 🧪 Installation locale (Mac/Linux)

```bash
# 1. Clone le projet
git clone https://github.com/ton-user/iam-backend.git
cd iam-backend

# 2. Crée un environnement virtuel
python3 -m venv iam-env
source iam-env/bin/activate

# 3. Installe les dépendances
pip install -r requirements.txt
