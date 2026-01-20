import pytesseract
from PIL import Image

# 👇 Cambia esto por la ruta donde instalaste Tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Cargar imagen
image_path = "C:\\Users\\Usuario\\Pictures\\comprobante.jpg"
image = Image.open(image_path)

# Extraer texto con OCR
texto_extraido = pytesseract.image_to_string(image, lang="eng")
print(texto_extraido)  # 'spa' = español
