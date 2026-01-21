import sys
from deep_translator import GoogleTranslator


def traduccionSpanish(text):
    traduccion = GoogleTranslator(source='en', target='es').translate(text)
    # Imprimir en consola asegurando UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    return traduccion


print(traduccionSpanish("""This site can’t be reached
xdataperu.com’s DNS address could not be found. Diagnosing the problem.
DNS_PROBE_POSSIBLE"""))  # → Éxito.
