from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
import time

# Configuración del navegador
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

# Ir a la página
driver.get("https://xdataperu.com/reniec-2025")

# Esperar que cargue todo
time.sleep(1)

# Ingresar DNI y tipo de consulta
dni = "77485004"

# Completar el formulario (asumiendo que hay inputs con IDs)
dni_input = driver.find_element('name', 'dato')
dni_input.send_keys(dni)

tipo_select = driver.find_element('name', 'tipo_consulta')
tipo_select.send_keys('reniec_online')

# Enviar formulario (asumiendo que hay un botón tipo submit)
submit_button = driver.find_element('xpath', '//button[@type="submit"]')
submit_button.click()

# Esperar a que cargue el resultado
time.sleep(3)

# Buscar imagen base64
img_tag = driver.find_element(
    'xpath', '//img[starts-with(@src, "data:image/jpeg;base64")]')
img_src = img_tag.get_attribute('src')

# Guardar imagen si existe
if img_src:
    base64_data = img_src.split(',')[1]
    image_data = base64.b64decode(base64_data)
    with open("foto.jpg", "wb") as f:
        f.write(image_data)
    print("✅ Imagen guardada como 'foto.jpg'")
else:
    print("❌ No se encontró imagen base64")

# Cerrar navegador
driver.quit()
