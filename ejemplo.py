import json
import requests


def consumir_api(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si la respuesta tiene un código de estado 4xx o 5xx
        datos = respuesta.json()  # Convierte la respuesta a JSON
        return datos
    except requests.exceptions.RequestException as e:
        print(f"Error al consumir la API: {e}")
        return None


if __name__ == "__main__":
    url = "http://127.0.0.1:8000/BookList/books"  # API de ejemplo
    respuesta = consumir_api(url)
    print(type(respuesta))
    print(respuesta["message"])
