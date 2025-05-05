from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def read_users():
    return {"message": "USERS"}

@router.get("/{user_id}")
def read_user_id(user_id: int):
    return {"user": f"User {user_id}"}