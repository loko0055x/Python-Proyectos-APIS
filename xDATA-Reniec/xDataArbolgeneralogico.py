import requests
from bs4 import BeautifulSoup
url = "https://xdataperu.com/consultaarbol"

# Datos que se enviarán
data = {
    "api_seleccionada": "agv",
    "dni": "40207286"
}

session = requests.Session()
response = session.post(url, data=data)

# Parsear HTML
soup = BeautifulSoup(response.text, "html.parser")

# Crear diccionario de resultados
resultado = {}

# Recorrer todos los elementos con texto
for label in soup.find_all(text=True):
    text = label.strip()
    if not text:
        continue
    # Buscar siguiente tag con contenido
    next_tag = label.find_next()
    if next_tag:
        valor = next_tag.get_text(strip=True)
        if valor:
            resultado[text] = valor

# Mostrar todos los datos
for k, v in resultado.items():
    print(f"{k}: {v}")
