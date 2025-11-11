from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
def get_items():
    return [
        {"id": 1, "name": "Teclado"},
        {"id": 2, "name": "Mouse"}
    ]
