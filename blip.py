from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import traductorFuncional as trx


# Cargar el modelo y el procesador
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")

# Abrir imagen local
image = Image.open("C:\\Users\\Usuario\\Pictures\\comprobante.jpg")

# Procesar la imagen y generar la descripción
inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

caption = trx.traduccionSpanish(caption)
print("Descripción:", caption)
