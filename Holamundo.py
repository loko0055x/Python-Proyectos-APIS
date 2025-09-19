
import whisper
import sys
import os
# Forzar UTF-8 en la salida estándar
sys.stdout.reconfigure(encoding='utf-8')

# Comprobar que se pasó un argumento


# Tomar la ruta del archivo del primer argumento
archivo_audio = sys.argv[1]
if not os.path.exists(archivo_audio):
    print(f"Error: no se encontró el archivo {archivo_audio}")
    sys.exit(1)
# Cargar modelo
model = whisper.load_model("tiny")

# Transcribir usando el argumento directamente
result = model.transcribe(archivo_audio)

# Imprimir solo el texto
print(result["text"])
