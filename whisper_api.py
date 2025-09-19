# Whisper + BLIP API
from fastapi import FastAPI
from pydantic import BaseModel
import base64
import whisper
import sys
import tempfile
import os
from io import BytesIO
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import traductorFuncional as trx

# Forzar UTF-8 en salida
sys.stdout.reconfigure(encoding="utf-8")

app = FastAPI()

# ---- Inicialización de modelos ----
whisper_model = whisper.load_model("tiny")
blip_processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")


# ---- Utilidades ----
def decode_base64(data: str) -> bytes:
    return base64.b64decode(data)


def image_from_base64(data: str) -> Image.Image:
    return Image.open(BytesIO(decode_base64(data)))


# ---- Schemas ----
class AudioRequest(BaseModel):
    audio_base64: str


class ImageRequest(BaseModel):
    imagen_base64: str


# ---- Endpoints ----
@app.post("/transcribe")
def transcribe_audio(req: AudioRequest):
    audio_bytes = decode_base64(req.audio_base64)

    # Guardar en archivo temporal (delete=False para que Whisper lo pueda leer en Windows)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".oga") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        result = whisper_model.transcribe(tmp_path)
    finally:
        # Siempre limpiar el archivo temporal
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return {"text": result["text"]}


@app.post("/getTextImg")
def transcribe_image(req: ImageRequest):
    image = image_from_base64(req.imagen_base64)
    inputs = blip_processor(image, return_tensors="pt")
    output = blip_model.generate(**inputs)
    caption = blip_processor.decode(output[0], skip_special_tokens=True)

    return {"text": trx.traduccionSpanish(caption)}
