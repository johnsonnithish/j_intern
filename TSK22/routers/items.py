from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def read_items():
    return [
            {"it_id": 1, "it_name": "item1"},
            {"it_id": 2, "it_name": "item2"},
            {"it_id": 3, "it_name": "item3"}
            ]

@router.get("/{item_id}")
def read_item_id(item_id: int):
    return [
            {"it_id": item_id, "it_name": f"item{item_id}"}
         ]

