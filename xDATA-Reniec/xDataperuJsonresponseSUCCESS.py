import requests
from bs4 import BeautifulSoup
import time
import re
import json

# URL de consulta
url = "https://xdataperu.com/reniec-2025"

# Datos que se enviarán
data = {
    "dato": "77485004",
    "tipo_consulta": "reniec_online"
}


def obtener_datos(session, url, data, reintentos=3, espera=2):
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


def limpiar_guion(texto):
    # Reemplaza cualquier guion "raro" por el normal -
    return re.sub(r'[-‐‑‒–—−]', '-', texto)


def extraer_dni_completo(soup):
    # Buscar etiquetas que contengan "DNI" en texto
    etiquetas_dni = soup.find_all(string=re.compile("DNI"))

    for etiqueta in etiquetas_dni:
        # Tomamos el texto de la etiqueta
        texto = etiqueta.strip()

        # Intentamos sacar el DNI completo del texto mismo
        texto = limpiar_guion(texto)
        match = re.search(r"\b(\d{8}-\d)\b", texto)
        if match:
            return match.group(1)

        # Si no está en el texto mismo, miramos el siguiente nodo (hermano)
        siguiente = etiqueta.find_next(string=True)
        if siguiente:
            concatenado = texto + " " + siguiente.strip()
            concatenado = limpiar_guion(concatenado)
            match = re.search(r"\b(\d{8}-\d)\b", concatenado)
            if match:
                return match.group(1)

    return None


def extraer_campos(soup, campos):
    resultado = {}
    for campo in campos:
        etiqueta = soup.find(string=re.compile(f"^{re.escape(campo)}"))
        if etiqueta:
            siguiente = etiqueta.find_next()
            if siguiente:
                valor = siguiente.get_text(separator=" ", strip=True)
                valor = re.sub(r'\s+', ' ', valor)
                resultado[campo] = valor
            else:
                resultado[campo] = ""
        else:
            resultado[campo] = ""
    return resultado


def main():
    session = requests.Session()
    html = obtener_datos(session, url, data)

    if not html:
        print("No se pudo obtener datos después de varios intentos.")
        return

    soup = BeautifulSoup(html, "html.parser")

    # Si hay un contenedor que limita la info, puedes usarlo para evitar duplicados,
    # Ejemplo: contenedor = soup.find("div", {"id": "main-content"})
    # Si no, usa todo el soup

    dni = extraer_dni_completo(soup)
    resultado = {}
    resultado["DNI"] = dni if dni else data["dato"]

    campos = [
        "Nombres", "Apellidos", "Fecha Nacimiento", "Estado Civil", "Dirección",
        "Ubigeo", "Padre", "Madre", "Fecha Inscripción", "Ubigeo Nacimiento", "Sexo"
    ]

    campos_extraidos = extraer_campos(soup, campos)
    resultado.update(campos_extraidos)

    print(json.dumps(resultado, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
