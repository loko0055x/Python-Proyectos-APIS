import requests
from bs4 import BeautifulSoup

session = requests.Session()

url_get = "https://xdataperu.com/reniec-2025"
response_get = session.get(url_get)
print("Status GET:", response_get.status_code)
print("Cookies:", session.cookies.get_dict())

soup = BeautifulSoup(response_get.text, "html.parser")
csrf_token = soup.find("input", {"name": "_token"})[
    "value"] if soup.find("input", {"name": "_token"}) else None

url_post = "https://xdataperu.com/reniec-2025"
payload = {
    "dato": "60537130",
    "tipo_consulta": "reniec_online"
}

# Si hay token CSRF
if csrf_token:
    payload["_token"] = csrf_token

response_post = session.post(url_post, data=payload)
print("Status POST:", response_post.status_code)
# solo primeros 500 caracteres
print("HTML o contenido recibido:", response_post.text[:500])


def renovar_sesion():
    response = session.get(url_get)
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "_token"})["value"] if soup.find(
        "input", {"name": "_token"}) else None
    return token
