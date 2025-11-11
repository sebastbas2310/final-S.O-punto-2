from fastapi import APIRouter
from models.person import Person
fake_person_db = [
    {"id": 1, "name": "Miguel", "age": 25},
    {"id": 2, "name": "Ana", "age": 30}
]
@router.get("/")
def get_persons():
    return fake_person_db
@router.get("/{person_id}")
def get_person(person_id: int):
    for p in fake_person_db:
@router.post("/")
def create_person(person: Person):
    fake_person_db.append(person.dict())
    return {"message": "Persona agregada correctamente", "data": person}
from fastapi import APIRouter
from models.person_model import Person

router = APIRouter(
    prefix="/person",
    tags=["person"]
)

fake_person_db = [
    {"id": 1, "name": "Miguel", "age": 25},
    {"id": 2, "name": "Ana", "age": 30}
]


@router.get("/")
def get_persons():
    return fake_person_db


@router.get("/{person_id}")
def get_person(person_id: int):
    for p in fake_person_db:
        if p["id"] == person_id:
            return p
    return {"error": "Persona no encontrada"}


@router.post("/")
def create_person(person: Person):
    fake_person_db.append(person.dict())
    return {"message": "Persona agregada correctamente", "data": person}
