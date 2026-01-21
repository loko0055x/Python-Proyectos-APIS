import requests

import json

"""
Consumo de api sobre los contactos que tengo en evolution api
sin que se repita por la foto
"""


def obtener_contactos():
    url = "http://192.168.18.102:3000/chat/findContacts/prueba"
    API_KEY = "1234"
    HEADERS = {"apikey": API_KEY, "Content-Type": "application/json"}
    response = requests.post(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener los contactos: {response.status_code}")
        return []


def main():
    contactos = obtener_contactos()
    unicos = {}

    for c in contactos:
        key = c.get('profilePicUrl') or c.get(
            'pushName')  # clave para comparar
        if key and (key not in unicos or c.get('remoteJid', '').endswith("@s.whatsapp.net")):
            unicos[key] = c

    return unicos


if __name__ == "__main__":
    contactos_filtrados = main()
    print(json.dumps(contactos_filtrados, indent=4, ensure_ascii=False))
