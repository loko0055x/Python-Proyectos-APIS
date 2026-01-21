import pytesseract
from PIL import Image


"""
¿Qué es Tesseract?

Tesseract es un motor OCR (uno de los más usados del mundo).
Fue creado por Google
Es open source
Lee texto en imágenes

📷 Foto de un documento → texto editable

🧾 Escanear una factura → copiar el texto

🖼️ Imagen con letras → string en Python


Mediante una ruta de imagen lo que hace es transcribir una imagen a texto
EXCLUSIVAMENTE  A METODOS DE PAGO
"""


# 👇 Cambia esto por la ruta donde instalaste Tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Cargar imagen
image_path = "C:\\Users\\Usuario\\Pictures\\comprobante.jpg"
image = Image.open(image_path)

# Extraer texto con OCR
texto_extraido = pytesseract.image_to_string(image, lang="eng")
print(texto_extraido)  # 'spa' = español
