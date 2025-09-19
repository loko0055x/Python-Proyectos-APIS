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

sys.stdout.reconfigure(encoding="utf-8")

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
