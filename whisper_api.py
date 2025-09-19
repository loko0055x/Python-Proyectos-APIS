# WhisperAPI
from fastapi import FastAPI
from pydantic import BaseModel
import base64
import whisper
import tempfile
import sys
import os
# Blip
import base64
from io import BytesIO
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import traductorFuncional as trx

# Forzar UTF-8
sys.stdout.reconfigure(encoding='utf-8')

app = FastAPI()
model = whisper.load_model("tiny")  # Carga el modelo una sola vez


class AudioRequest(BaseModel):
    audio_base64: str


@app.post("/transcribe")
def transcribe_audio(req: AudioRequest):
    # Decodificar base64 a bytes
    audio_bytes = base64.b64decode(req.audio_base64)

    # Guardar temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".oga") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    # Transcribir
    result = model.transcribe(tmp_path)

    # Borrar archivo temporal
    os.remove(tmp_path)

    # Retornar solo el texto
    return {"text": result["text"]}


def image_from_base64(base64_string):
    image_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(image_data))


# Cargar BLIP
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")


class ImagenRequest(BaseModel):
    imagen_base64: str


@app.post("/getTextImg")
def transcribe_Imagen(req: ImagenRequest):

    # Convertir base64 a imagen
    image = image_from_base64(req.imagen_base64)
# Procesar con BLIP
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

# Traducir al español
    caption = trx.traduccionSpanish(caption)
    return {"text": caption}
