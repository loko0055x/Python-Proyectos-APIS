import requests

HEADERS = {"User-Agent": "MiPracticaDeScrapingBot/1.0 (+tu_email@ejemplo.com)"}
url = "https://xdataperu.com/reniec-2025"
data = {"dato": "77485004", "tipo_consulta": "reniec_online"}

resp = requests.post(url, data=data, headers=HEADERS, timeout=10)
print("Código:", resp.status_code)
print("Encabezados de respuesta:")
for k, v in resp.headers.items():
    print(k+":", v)
# Ver si el HTML refleja tu user-agent o IP (peligro: si aparece, es información visible)
html = resp.text
if "MiPracticaDeScrapingBot" in html:
    print("El HTML contiene tu User-Agent.")
else:
    print("No se ve tu User-Agent en el HTML.")
