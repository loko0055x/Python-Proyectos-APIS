import sys
from deep_translator import GoogleTranslator


def traduccionSpanish(text):
    traduccion = GoogleTranslator(source='en', target='es').translate(text)
    # Imprimir en consola asegurando UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    return traduccion


# print(traduccionSpanish("Success"))  # → Éxito.
