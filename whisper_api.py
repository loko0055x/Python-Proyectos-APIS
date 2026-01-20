from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import base64
import tempfile
import os
import sys
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from transformers import BlipProcessor, BlipForConditionalGeneration
import whisper
import traductorFuncional as trx
import pytesseract
from youtube_transcript_api import YouTubeTranscriptApi
import getRemoteIDFunction as api_remote
sys.stdout.reconfigure(encoding="utf-8")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


app = FastAPI()

# --- Cargar modelos una sola vez ---
try:
    whisper_model = whisper.load_model("tiny")
    blip_processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base")
    blip_model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base")
    print("Modelos cargados correctamente.")
except Exception as e:
    print("Error cargando modelos:", e)
    raise


# --- Schemas ---
class AudioRequest(BaseModel):
    audio_base64: str


class ImageRequest(BaseModel):
    imagen_base64: str


# metodos
def decode_base64_to_image(base64_str: str) -> Image.Image:
    try:
        img_bytes = base64.b64decode(base64_str)
        return Image.open(BytesIO(img_bytes)).convert("RGB")
    except Exception as e:
        raise ValueError("Imagen base64 inválida o corrupta") from e


# --- Endpoints ---
@app.post("/transcribe")
def transcribe_audio(req: AudioRequest):
    try:
        audio_bytes = base64.b64decode(req.audio_base64)
    except Exception:
        return JSONResponse(status_code=400, content={"ok": False, "error": "Audio base64 inválido"})

    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".oga") as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        result = whisper_model.transcribe(tmp_path)
        return JSONResponse(status_code=200, content={"ok": True, "text": result.get("text", "")})

    except Exception as e:
        return JSONResponse(status_code=500, content={"ok": False, "error": str(e)})

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)


@app.post("/getTextImg")
def transcribe_image(req: ImageRequest):
    try:
        img_bytes = base64.b64decode(req.imagen_base64)
        image = Image.open(BytesIO(img_bytes)).convert("RGB")
    except (Exception, UnidentifiedImageError):
        return JSONResponse(status_code=400, content={"ok": False, "error": "Imagen base64 inválida o corrupta"})

    try:
        inputs = blip_processor(image, return_tensors="pt")
        output = blip_model.generate(**inputs)
        caption = blip_processor.decode(output[0], skip_special_tokens=True)

        # Intentar traducir, pero si falla devolver original
        try:
            caption = trx.traduccionSpanish(caption)
        except Exception:
            pass

        return JSONResponse(status_code=200, content={"ok": True, "text": caption})

    except Exception as e:
        return JSONResponse(status_code=500, content={"ok": False, "error": str(e)})


@app.post("/getTextVoucher")
def transcribe_voucher(req: ImageRequest):
    try:
        img_bytes = base64.b64decode(req.imagen_base64)
        image = Image.open(BytesIO(img_bytes)).convert("RGB")
    except (Exception, UnidentifiedImageError):
        return JSONResponse(status_code=400, content={"ok": False, "error": "Imagen base64 inválida o corrupta"})

    try:

        texto_extraido = pytesseract.image_to_string(image, lang="eng")

        return JSONResponse(status_code=200, content={"ok": True, "text": texto_extraido})

    except Exception as e:
        return JSONResponse(status_code=500, content={"ok": False, "error": str(e)})


class RemoteIDRequest(BaseModel):
    remoteJid: str
    pushName: str | None = None
    
@app.post("/getRemoteID")

def get_remote_id(req: RemoteIDRequest):
    try:
        jid_original = req.remoteJid
        push_name = req.pushName

        jid_resuelto = api_remote.normalizar_jid(jid_original, push_name)

        return JSONResponse(
            status_code=200,
            content={
                "ok": True,
                "uidbasic": jid_original,
                "remoteID": jid_resuelto,
                "resolved": jid_original != jid_resuelto
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"ok": False, "error": str(e)}
        )