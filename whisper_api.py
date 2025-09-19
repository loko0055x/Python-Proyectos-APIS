from fastapi import FastAPI
from pydantic import BaseModel
import base64
import whisper
import tempfile
import sys
import os

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


class ImagenRequest(BaseModel):
    imagen_base64: str


@app.post("/getTextImg")
def transcribe_Imagen(req: ImagenRequest):
    # Decodificar base64 a bytes
    Img_bytes = base64.b64decode(req.imagen_base64)
