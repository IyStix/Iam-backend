import os

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    LDAP_SERVER = "ldap://your-ldap-server"
    LDAP_BASE_DN = "dc=epita,dc=fr"

settings = Settings()
