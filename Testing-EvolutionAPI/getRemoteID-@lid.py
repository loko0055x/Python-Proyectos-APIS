import requests
import json

"""
Usando Evolution API 
Mediante un  pushName  te retorna el  @s.whatsapp.net
pero solo mediante el push name nada mas
"""




API_URL = "http://192.168.18.102:3000"
INSTANCE = "prueba"
API_KEY = "1234"
headers = {"apikey": API_KEY, "Content-Type": "application/json"}






def find_all_contacts():
    r = requests.post(f"{API_URL}/chat/findContacts/{INSTANCE}",
                      headers=headers, json={"where": {}})
    return r.json() if r.ok else []


def normalizar_jid(jid, push_name=None):
    # si no es LID, devolver directo
    if not jid.endswith("@lid"):
        return jid

    contactos = find_all_contacts()
    if not contactos:
        return jid

    # 1️⃣ intenta emparejar por pushName
    if push_name:
        for c in contactos:
            if c.get("pushName") == push_name and c["remoteJid"].endswith("@s.whatsapp.net"):
                return c["remoteJid"]

    # 2️⃣ intenta emparejar por foto de perfil (solo si existe)
    for c in contactos:
        if c["remoteJid"].endswith("@s.whatsapp.net") and "profilePicUrl" in c:
            # aquí podrías comparar URLs si tu webhook las incluye
            pass

    # 3️⃣ fallback → no encontrado
    return jid


# --- ejemplo de uso ---
webhook = {
    "key": {"remoteJid": "131142682415195@lid"},
    "pushName": "Mama",
}

webhook = {
    "key": {"remoteJid": "268113450905721@lid"},
    "pushName": "< David />",
}
jid_original = webhook["key"]["remoteJid"]
push_name = webhook.get("pushName")

jid_resuelto = normalizar_jid(jid_original, push_name)
print("🔍 JID ORIGINAL:", jid_original)
print("✅ JID NORMALIZADO:", jid_resuelto)
