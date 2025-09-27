import requests
from bs4 import BeautifulSoup

# URL de la página
url = "https://xdataperu.com/reniec-2025"

# Datos a enviar en POST
data = {
    "dato": "77485004",  # DNI a consultar
    "tipo_consulta": "reniec_online"
}

# Crear sesión
session = requests.Session()

# Hacer POST
response = session.post(url, data=data)

# Parsear HTML
soup = BeautifulSoup(response.text, "html.parser")

# Buscar la tabla de resultados
tabla = soup.find("table", class_="result-table")

# Verificamos que la tabla exista
if not tabla:
    print("No se encontró la tabla de resultados.")
    exit()

# Extraer todos los <th> y <td> como pares clave-valor
datos = {}
for fila in tabla.find_all("tr"):
    th = fila.find("th")
    td = fila.find("td")
    if th and td:
        clave = th.get_text(strip=True)
        valor = td.get_text(" ", strip=True)
        datos[clave] = valor

# Mostrar resultados
for campo, valor in datos.items():
    print(f"{campo}: {valor}")
