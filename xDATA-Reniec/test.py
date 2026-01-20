import requests
from bs4 import BeautifulSoup
import base64

# URL del endpoint
url = "https://xdataperu.com/consultaarbol"

# Datos a enviar
data = {
    "api_seleccionada": "agv",
    "dni": "40207286"
}

# Headers para simular navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://xdataperu.com",
    "Referer": "https://xdataperu.com/consultaarbol",
    # "Cookie": "session=.eJxFjkEKwyAQRe8y6ySoqTW66qJH6F4kDiIYLcaUQOndOwmFLv_w5v3_BlxcTGDAlx2LkvwWsNSAw1wW6AD3Z6y4WtcIEUzInuleqAfXRmgj-XCR45ULIqMHM0o98Q6SW5utmCPOxwsYrqRmTCqlBmqYKBFUQkAfM5hWN-wguwWp4_6bQca_wc5ly7RA0LGkA9tWrIS8XIrenuHUfL6Xej3P.aNiAMA.qp6v3G8oo8pUgEAVBqtuGe6_iQk"

}

# Hacer la solicitud POST
response = requests.post(url, data=data, headers=headers)

if response.status_code == 200:
    # Parsear el HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar la imagen dentro del modal
    img_tag = soup.find("img", id="result-image")

    if img_tag and 'src' in img_tag.attrs:
        # Extraer la parte base64
        # separa "data:image/png;base64," del contenido
        image_base64 = img_tag['src'].split(",")[1]
        # Decodificar la imagen
        image_data = base64.b64decode(image_base64)
        print(image_base64)

        # Guardar en archivo
        with open("resultado.png", "wb") as f:
            f.write(image_data)

        print("Imagen guardada correctamente como 'resultado.png'.")
    else:
        print("No se encontró la imagen en el modal.")
else:
    print("Error en la solicitud:", response.status_code)
