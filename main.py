from fastapi import FastAPI, HTTPException
from models.schema_person import Person
from utils.s3_helper import read_csv_from_s3, write_csv_to_s3
import os
from routers.person_router import router as person_router


app = FastAPI(title="API con FastAPI y S3")

# S3 configuration via environment variable BUCKET_NAME
BUCKET_NAME = os.getenv("BUCKET_NAME", "tu-bucket-s3")
# fixed key for the CSV file (only one file exists at a time)
CSV_KEY = "persons.csv"


@app.post("/persons")
def add_person(person: Person):
    """Recibe una persona (nombre, edad, altura), valida con Pydantic,
    actualiza (o crea) el archivo CSV en S3 sobrescribiendo el mismo recurso.
    """
    try:
        # Leer filas existentes (si hay)
        rows, headers = read_csv_from_s3(BUCKET_NAME, CSV_KEY)
    except FileNotFoundError:
        rows = []
        headers = ["nombre", "edad", "altura"]

    # Append new row as dict in consistent order
    new_row = {"nombre": person.nombre, "edad": person.edad, "altura": person.altura}
    rows.append(new_row)

    # Escribir de nuevo el CSV (sobrescribe)
    write_csv_to_s3(BUCKET_NAME, CSV_KEY, rows, headers)

    return {"message": "Persona agregada correctamente", "total_rows": len(rows)}


@app.get("/persons/count")
def get_persons_count():
    """Retorna el número de filas del CSV almacenado en S3.
    Si el archivo no existe retorna 0.
    """
    try:
        rows, headers = read_csv_from_s3(BUCKET_NAME, CSV_KEY)
        return {"count": len(rows)}
    except FileNotFoundError:
        return {"count": 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# include the person router (prefix /person)
app.include_router(person_router)
