from flask import Flask, request
import requests
import json
from getRemoteIDFunction import returndata


app = Flask(__name__)

procesados = set()

# Configuración API Evolution
API_URL = "http://localhost:3000"
INSTANCE = "prueba"
API_KEY = "1234"
HEADERS = {"apikey": API_KEY, "Content-Type": "application/json"}


def sendMessage(number):
    payload = {
        "number":  number,
        "text": "Hola desde visual codexxxxxxxx"
    }

    print("📤 Enviando mensaje automático...")
    r = requests.post(f"{API_URL}/message/sendText/{INSTANCE}",
                      headers=HEADERS, json=payload)

    print(f"✅ Resultado del envío: {r.status_code} -> {r.text}")

    return {"status": "ok"}


@app.route("/webhook-test/evolution15-06-2025", methods=["POST"])
def evolution_webhook():
    data = request.json

    # 📩 Mostrar SIEMPRE el JSON recibido para debug
    print("📩 Webhook recibido crudo:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    # 🧪 Verificar tipo de evento
    event = data.get("event")
    if event != "messages.upsert":
        print(f"🚫 Ignorado evento tipo: {event}")
        return {"status": "ignored"}

    # Extraer información útil
    message_data = data.get("data", {})
    message_id = message_data.get("key", {}).get("id")
    status = message_data.get("status")

    # 🚫 Ignorar ACK o estados que no son mensajes nuevos
    if status and status != "PENDING":
        print("🚫 ACK ignorado")
        return {"status": "ack_ignored"}

    # ⏩ Verificar si ya procesamos este mensaje
    if message_id in procesados:
        print(f"⏩ Mensaje duplicado ignorado: {message_id}")
        return {"status": "duplicate_ignored"}
    procesados.add(message_id)

    # ✅ Mensaje NUEVO real -> aquí lo procesas
    remoteID = message_data.get("key", {}).get("remoteJid")
    pushName = message_data.get("pushName")
    conversation = message_data.get("message", {}).get("conversation")

    print("\n✅ MENSAJE NUEVO DETECTADO:")
    print(f"👤 Nombre: {pushName}")
    print(f"📱 Remitente: {remoteID}")
    print(f"💬 Mensaje: {conversation}\n")

    # 📤 Aquí podrías llamar a sendMessage() si lo necesitas
    return {"status": "ok", "message_id": message_id}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678, debug=True)


if __name__ == "__main__":
    # Servidor escuchando en tu puerto del webhook
    app.run(host="0.0.0.0", port=5678)
