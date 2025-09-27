
import requests
from bs4 import BeautifulSoup
import time

# URL de consulta
url = "https://xdataperu.com/reniec-2025"

# Datos que se enviarán
data = {
    "dato": "77485004",
    "tipo_consulta": "reniec_online"
}

# Función para obtener la página con manejo de sesión


def obtener_datos(session, url, data, reintentos=3, espera=2):
    """
    session: requests.Session()
    url: URL a consultar
    data: Diccionario con POST data
    reintentos: cantidad de reintentos si falla
    espera: segundos de espera entre reintentos
    """
    for intento in range(reintentos):
        try:
            response = session.post(url, data=data)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Intento {intento+1}: status {response.status_code}")
        except Exception as e:
            print(f"Intento {intento+1}: error {e}")
        time.sleep(espera)
    return None


# Crear sesión
session = requests.Session()

# Obtener HTML
html = obtener_datos(session, url, data)

if html:
    soup = BeautifulSoup(html, "html.parser")

    # Crear diccionario de resultados
    resultado = {}
    for label in soup.find_all(text=True):
        text = label.strip()
        if not text:
            continue
        next_tag = label.find_next()
        if next_tag:
            valor = next_tag.get_text(strip=True)
            if valor:
                resultado[text] = valor

    # Mostrar todos los datos
    for k, v in resultado.items():
        print(f"{k}: {v}")
else:
    print("No se pudo obtener datos después de varios intentos.")
