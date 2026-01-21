from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript
import json

"""
Este Proyecto trata de que mediante un link de youtube 
un uid te retorne en consola los subtitulos en español

 
"""


def verificar_video(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcripts = api.list(video_id)
        print(
            f"✅ El video '{video_id}' existe y tiene subtítulos disponiblesx:")
        print(transcripts)
        for t in transcripts:
            print(f" - {t.language} ({t.language_code})")

    except CouldNotRetrieveTranscript:
        print("❌ El video no existe, es privado o no está disponible.")
    except TranscriptsDisabled:
        print("⚠️ El video existe, pero los subtítulos están deshabilitados.")
    except NoTranscriptFound:
        print("⚠️ El video existe, pero no tiene subtítulos disponibles.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")


def tiene_subtitulos_es(video_id):
    try:
        api = YouTubeTranscriptApi()
        api.fetch(video_id, languages=['es'])
        print("Entro aqui")
        return {
            "success": True,
            "msg": "Si hay subtitulos en español",
        }
    except Exception as e:

        return {
            "success": False,
            "msg":   (f"⚠️ Error inesperado: {e}")

        }


def verificar_subtitulos(video_id):
    try:
        # Crear una instancia de la clase antes de llamar a list()
        api = YouTubeTranscriptApi()
        transcripts = api.list(video_id)

        print(f"Subtítulos encontrados para el video {video_id}:")
        for t in transcripts:
            print(f" - {t.language} ({t.language_code})")

    except TranscriptsDisabled:
        print("❌ Los subtítulos están deshabilitados para este video.")
    except NoTranscriptFound:
        print("⚠️ No se encontraron subtítulos disponibles.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")


def subtitulos_ingles(uid):

    video_id = uid  # ✅ solo el ID
    transcript = YouTubeTranscriptApi().fetch(video_id)

    for entry in transcript:
        print(f"{entry.start:.2f}s → {entry.text}")


def subtitulos_Español(uid):

    video_id = uid
    transcript = YouTubeTranscriptApi().fetch(video_id, languages=['es'])

    for entry in transcript:
        print(entry)


def subtitulos_EspañolJsonResponse(uid):
    containsubtitle = tiene_subtitulos_es(uid)
    if (containsubtitle["success"]):
        video_id = uid
        transcript = YouTubeTranscriptApi().fetch(video_id, languages=['es'])
        return (transcript)
    else:
        print("No tiene sub titulos")
    return "None"


def verificar_y_obtener_subtitulos(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcripts = api.list(video_id)
        print(
            f"✅ El video '{video_id}' existe y tiene subtítulos disponibles:\n")

        for t in transcripts:
            print(f"Idioma: {t.language}")
            print(f"Código: {t.language_code}")
            print(f"¿Automático?: {'Sí' if t.is_generated else 'No'}")
            print(
                f"¿Traducciones disponibles?: {'Sí' if t.is_translatable else 'No'}")
            print("-" * 40)

            # 📥 Obtener el contenido real del subtítulo
            try:
                data = t.fetch()  # devuelve objetos tipo FetchedTranscriptSnippet
                print("Ejemplo de subtítulos:")
                # solo los primeros 5 fragmentos
                for i, entry in enumerate(data):
                    print(f"{entry.start:.1f}s: {entry.text}")
                print("=" * 60)
            except Exception as e:
                print(f"⚠️ No se pudieron obtener subtítulos: {e}")
                print("=" * 60)

    except CouldNotRetrieveTranscript:
        print("❌ El video no existe, es privado o no está disponible.")
    except TranscriptsDisabled:
        print("⚠️ El video existe, pero los subtítulos están deshabilitados.")
    except NoTranscriptFound:
        print("⚠️ El video existe, pero no tiene subtítulos disponibles.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

# 🧪 Prueba


# verificar_y_obtener_subtitulos("JsGJQu6mjYs")
# print(verificar_video("JsGJQu6mjYs"))
print(subtitulos_EspañolJsonResponse("JsGJQu6mjYs"))
# print(tiene_subtitulos_es("JsGJQu6mjYs"))
