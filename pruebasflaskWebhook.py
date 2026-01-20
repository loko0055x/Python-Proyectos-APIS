from flask import Flask, request
import requests
import json
import getRemoteIDFunction as pbt  # tu módulo para normalizar el JID

app = Flask(__name__)

# --- CONFIGURACIÓN EVOLUTION API ---
API_URL = "http://localhost:3000"
INSTANCE = "prueba"
API_KEY = "1234"
HEADERS = {"apikey": API_KEY, "Content-Type": "application/json"}


def sendMessage(remitente):
    """Envía un mensaje a un número determinado"""
    payload = {
        "number": remitente,
        "text": "Hola soy IA 🤖, recibí tu mensaje!"
    }
    print(f"📤 Enviando respuesta a {remitente}...")
    r = requests.post(f"{API_URL}/message/sendText/{INSTANCE}",
                      headers=HEADERS, json=payload)
    print(f"✅ Respuesta enviada: {r.status_code} -> {r.text}")


@app.route("/webhook/evolution15-06-2025", methods=["POST"])
def evolution_webhook():
    data = request.json
    print("📩 Webhook recibido:\n", json.dumps(
        data, indent=4, ensure_ascii=False))

    if data.get("event") == "messages.upsert":
        message_data = data.get("data", {})
        key = message_data.get("key", {})
        from_me = key.get("fromMe", False)
        remitente = key.get("remoteJid", "")
        msg_id = key.get("id")

        # ⚠️ Ignorar mensajes de tipo LID (vienen de dispositivos vinculados)
        if "@lid" in remitente:
            print(f"⚠️ Ignorado evento con LID ({remitente})")
            return {"status": "ignored_lid"}

        # ⚠️ Ignorar si el mensaje es mío
        if from_me:
            print("⚠️ Ignorado mensaje enviado por mí mismo.")
            return {"status": "ignored_from_me"}

        mensaje = message_data.get("message", {}).get("conversation", "")
        nombre = message_data.get("pushName", "Desconocido")

        print(f"💬 {nombre} ({remitente}) dijo: {mensaje}")

        # ✅ Procesar solo mensajes reales (sin @lid)
        webhook = {"key": {"remoteJid": remitente}, "pushName": nombre}
       #  result = pbt.returndata(webhook)
        print("Enviando mensaje desde xDDDDDDD"+remitente)
      #  sendMessage(result["remoteID"])

        return {"status": "ok"}
    return {"status": "ignored"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678)
