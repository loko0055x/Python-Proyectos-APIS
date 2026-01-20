from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# --- CONFIGURACIÓN FIREFOX + GECKODRIVER ---
GECKO_PATH = r"C:\Users\Usuario\Downloads\geckodriver.exe"
service = Service(executable_path=GECKO_PATH)
driver = webdriver.Firefox(service=service)

try:
    # Abrir página de login
    driver.get("https://xdataperu.com/login")

    # Esperar campos de login
    # hasta 2 minutos para que resuelvas reCAPTCHA
    wait = WebDriverWait(driver, 120)
    user_input_field = wait.until(
        EC.presence_of_element_located((By.ID, "user_input")))
    password_field = driver.find_element(By.ID, "pasword")

    # Ingresar tus credenciales
    user_input_field.send_keys("doxeo751@george.com")
    password_field.send_keys("826373")

    print("Resuelve el reCAPTCHA y haz click en 'Ingresar' en Firefox...")

    # Esperar hasta que cambie la URL o aparezca un elemento del dashboard
    wait.until(lambda d: d.current_url != "https://xdataperu.com/login")
    print("Login detectado, extrayendo cookies para la API...")

    # --- EXTRAER COOKIES DE SELENIUM ---
    selenium_cookies = driver.get_cookies()
    cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}

    # User-Agent desde Selenium
    user_agent = driver.execute_script("return navigator.userAgent;")
    headers = {
        "User-Agent": user_agent,
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest"
    }

    # --- DATOS DE LA API ---
    api_url = "https://xdataperu.com/consultaarbol"
    data = {
        "api_seleccionada": "agv",
        "dni": "12345678"
    }

    # Consumir la API usando cookies de sesión
    response = requests.post(
        api_url, data=data, cookies=cookies, headers=headers)

    # Mostrar respuesta
    print("Respuesta de la API:")
    print(response.text)

finally:
    time.sleep(5)  # opcional: para ver Firefox antes de cerrar
    driver.quit()
