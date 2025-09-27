import requests
from bs4 import BeautifulSoup

# URL de la página
url = "https://xdataperu.com/reniec-2025"

# Datos a enviar en POST
data = {
    "dato": "949273071",  # DNI a consultar
    "tipo_consulta": "telefono_online"
}

# Crear sesión
session = requests.Session()

# Hacer POST
response = session.post(url, data=data)

# Parsear HTML
soup = BeautifulSoup(response.text, "html.parser")

# Buscar la tabla de resultados
tabla = soup.find("table", class_="telefono-table")

# Verificamos que la tabla exista
if not tabla:
    print("No se encontró la tabla de resultados.")
    exit()

# Buscar todas las filas dentro del cuerpo de la tabla
filas = tabla.find("tbody").find_all("tr")

# Extraer los datos de cada fila
for fila in filas:
    celdas = fila.find_all("td")
    if celdas:
        telefono = celdas[0].get_text(strip=True)
        dni = celdas[1].get_text(strip=True)
        nombres = celdas[2].get_text(strip=True)
        apellidos = celdas[3].get_text(strip=True)

        # Mostrar los resultados
        print(f"Teléfono: {telefono}")
        print(f"DNI: {dni}")
        print(f"Nombres: {nombres if nombres else 'No disponible'}")
        print(f"Apellidos: {apellidos if apellidos else 'No disponible'}")
        print("-" * 30)
