import sys
from deep_translator import GoogleTranslator


def traduccionSpanish(text):
    traduccion = GoogleTranslator(source='en', target='es').translate(text)
    # Imprimir en consola asegurando UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    return traduccion


print(traduccionSpanish("""Your n8n server is configured to use a secure cookie,
however you are either visiting this via an insecure URL, or using Safari.

To fix this, please consider the following options:
Setup TLS/HTTPS (recommended), or
If you are running this locally, and not using Safari, try using localhost instead
If you prefer to disable this security feature (not recommended), set the environment variable N8N_SECURE_COOKIE to false"""))  # → Éxito.
