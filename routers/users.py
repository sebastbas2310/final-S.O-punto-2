from fastapi import APIRouter
from fastapi import APIRouter
from models.person_model import Person

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

fake_users_db = [
    {"id": 1, "name": "Miguel", "age": 25},
    {"id": 2, "name": "Ana", "age": 30}
]

@router.get("/")
def get_users():
    return fake_users_db

@router.get("/{user_id}")
def get_user(user_id: int):
    for user in fake_users_db:
        if user["id"] == user_id:
            return user
    return {"error": "Usuario no encontrado"}

@router.post("/")
def create_user(person: Person):
    fake_users_db.append(person.dict())
    return {"message": "Usuario agregado correctamente", "data": person}
