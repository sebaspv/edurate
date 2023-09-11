import fire
import uvicorn
from src.api.app import app
import requests

class Edurate(object):
  def add(self, escuela, nombre):
    base_url = 'http://0.0.0.0:8000/profesor'
    params = {'escuela': escuela, 'profesor': nombre}
    url = f'{base_url}?escuela={params["escuela"]}&profesor={params["profesor"]}'
    headers = {'accept': 'application/json'}
    response = requests.post(url, headers=headers)
    resultado = response.json()
    calif = resultado["calificación"]
    print(f"Se ha añadido al profesor {nombre} con calificación {calif}")
  def ver(self):
    base_url = 'http://0.0.0.0:8000/profesor'
    url = f'{base_url}'
    headers = {'accept': 'application/json'}
    response = requests.get(url).json()
    for name, info in response.items():
      calificacion = info.get("calificación")
      print(f"{name}: {calificacion}")

if __name__ == '__main__':
  fire.Fire(Edurate)