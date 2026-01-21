import requests
import json

"""
API SOBRE DEPARTAMENTOS PRONVINCIAS Y DISTRITOS DE LIMA PERU 
"""

def obtener_data(ruta):
    url = ruta
    API_KEY = "1234"
    HEADERS = {"apikey": API_KEY, "Content-Type": "application/json"}
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()  # Esto es un dict

        # print(json.dumps(response.json(), indent=4))
        return data
    else:
        print(f"Error al obtener los contactos: {response.status_code}")
        return []





departamentolink = "https://raw.githubusercontent.com/ernestorivero/Ubigeo-Peru/master/json/ubigeo_peru_2016_departamentos.json"
provincialink = "https://raw.githubusercontent.com/ernestorivero/Ubigeo-Peru/master/json/ubigeo_peru_2016_provincias.json"
distriolink = "https://raw.githubusercontent.com/ernestorivero/Ubigeo-Peru/master/json/ubigeo_peru_2016_distritos.json"


listdepa = obtener_data(departamentolink)
listprov = obtener_data(provincialink)
listdistrito = obtener_data(distriolink)

print((listdepa)[0]["id"])


# result = filter((lambda x: x["department_id"] == "01"), listprov)
result = filter((lambda x: x["province_id"] ==
                "2502" and x["department_id"] == "25"), listdistrito)

print(list(result))

# filter((lambda x:  x % 2 == 0), arreglo)
