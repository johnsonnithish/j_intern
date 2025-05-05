from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def read_items():
    return {"message": "ITEMS"}

@router.get("/{item_id}")
def read_item_id(item_id: int):
    return {"item": f"Item {item_id}"}

