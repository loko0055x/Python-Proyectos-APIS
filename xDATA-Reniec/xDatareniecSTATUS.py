import requests
from bs4 import BeautifulSoup

# URL de la API
api_url = "https://xdataperu.com/reniec-2025"  # Cambia esto si es diferente

# Datos que se enviarán en la solicitud POST
data = {
    "dato": "60537130",       # DNI u otro dato
    "tipo_consulta": "reniec_online"  # Tipo de consulta
}

# Hacer la solicitud POST
response = requests.post(api_url, data=data)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print(f"Solicitud exitosa. Código de estado: {response.status_code}")

    # Obtener el contenido HTML
    content = response.text

    # Buscar si hay un mensaje que indique que el DNI es inválido
    if "DNI inválido" in content:
        print("El DNI proporcionado es inválido.")
    else:
        print("DNI válido. Mostrando los resultados...")

        # Usar BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(content, "html.parser")

        # Buscar el modal que contiene los resultados de la consulta
        modal = soup.find(id="resultModal")
        if modal:
            print("Contenido del modal encontrado:")
            # Muestra el HTML del modal (imagen base64, botones, etc.)
            print(modal.prettify())

            # Si el modal contiene la imagen en base64, extraerla
            img_tag = modal.find("img")
            if img_tag and 'src' in img_tag.attrs:
                image_base64 = img_tag.attrs['src']
                print(f"Imagen en base64: {image_base64}")
            else:
                print("No se encontró la imagen en el modal.")
        else:
            print("No se encontraron resultados en el modal.")
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
