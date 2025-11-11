from pydantic import BaseModel

class Person(BaseModel):
    nombre: str
    edad: int
    altura: float
