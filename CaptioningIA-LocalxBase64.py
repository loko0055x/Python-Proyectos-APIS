import base64
from io import BytesIO
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import traductorFuncional as trx

# Cargar BLIP
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")

# 👉 Supongamos que ya tienes la imagen en base64 en esta variable

# /////////////////////////////////////////////////////////////
archivo_sin_leer = open(
    "imagen_base64.txt")
linea = archivo_sin_leer.readline()
archivo_sin_leer.close()


# //////////////////////////////////////////////////////////////

base64_img = linea  # <- tu string base64 real aquí

# Función para convertir base64 → PIL.Image


def image_from_base64(base64_string):
    image_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(image_data))


# Convertir base64 a imagen
image = image_from_base64(base64_img)

# Procesar con BLIP
inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

# Traducir al español
caption = trx.traduccionSpanish(caption)
print("Descripción:", caption)
