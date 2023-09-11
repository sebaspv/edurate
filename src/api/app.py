from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
from .scrape_profesores import calificacion_profe
from sqlitedict import SqliteDict

app = FastAPI()
db = SqliteDict("profesores.sqlite")
@app.post("/profesor")
async def escuela(escuela: str, profesor: str) -> dict:
    calificacion = calificacion_profe(escuela, profesor)
    db[profesor] = calificacion
    db.commit()
    return calificacion

@app.get("/profesor")
async def profesores() -> dict:
    data = db
    return data

@app.get("/profesor/{nombre}")
async def profesor(nombre) -> dict:
    data = db
    return data[nombre]

@app.delete("/profesor/{nombre}")
async def quitarprofe(nombre) -> dict:
    del db[nombre]
    return db