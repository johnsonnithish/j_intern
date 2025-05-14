from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def read_users():
    return [
            {"user_id": 1, "user_name": "user1"},
            {"user_id": 2, "user_name": "user2"},
            {"user_id": 3, "user_name": "user3"}
            ]

@router.get("/{user_id}")
def read_user_id(user_id: int):
    return [
            {"user_id": user_id, "user_name": f"user{user_id}"}
            ]
