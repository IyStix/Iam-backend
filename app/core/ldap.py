from ldap3 import Server, Connection, ALL
import os

LDAP_SERVER = os.getenv("LDAP_SERVER", "ldap://localhost")
LDAP_BASE_DN = os.getenv("LDAP_BASE_DN", "dc=epita,dc=fr")

def ldap_authenticate(username: str, password: str) -> bool:
    try:
        user_dn = f"uid={username},{LDAP_BASE_DN}"
        server = Server(LDAP_SERVER, get_info=ALL)
        conn = Connection(server, user=user_dn, password=password, auto_bind=True)
        return True
    except Exception:
        return False
