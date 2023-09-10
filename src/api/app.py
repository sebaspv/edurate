from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
async def escuela(nombre: str) -> dict:
    nombre_amigable_url = nombre.replace(" ", "+")
    URL = f"https://www.misprofesores.com/Buscar?q={nombre_amigable_url}"
    contenido = requests.get(URL)
    soup = BeautifulSoup(contenido.content, "html.parser")
    return {"nombre": nombre}