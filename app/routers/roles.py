from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_roles():
    return [{"role": "admin"}, {"role": "user"}]
