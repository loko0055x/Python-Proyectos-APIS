import sys
import io
from transformers import MarianMTModel, MarianTokenizer

# Forzar salida UTF-8 en Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Cargar modelo y tokenizer una sola vez
modelo_nombre = "Helsinki-NLP/opus-mt-en-es"
tokenizer = MarianTokenizer.from_pretrained(modelo_nombre)
model = MarianMTModel.from_pretrained(modelo_nombre)


def traducir_a_espanol(texto):
    tokens = tokenizer(texto, return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)


# Ahora esto será mucho más rápido
caption_en = "Success"
caption_es = traducir_a_espanol(caption_en)
print("Descripción en español:", caption_es)
