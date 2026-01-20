import requests
import json
import time

API_URL = "http://192.168.18.102:3000"
INSTANCE = "prueba"
API_KEY = "1234"
HEADERS = {"apikey": API_KEY, "Content-Type": "application/json"}

# 🧠 Cache global de contactos
_contact_cache = {
    "data": [],
    "last_update": 0,
    "ttl": 300  # tiempo de vida del caché en segundos (5 minutos)
}


def find_all_contacts(force=False):
    """
    Obtiene todos los contactos de Evolution API.
    Usa cache salvo que haya pasado el TTL o se fuerce la actualización.
    """
    global _contact_cache
    now = time.time()

    # ✅ Usa caché si sigue fresco
    if not force and _contact_cache["data"] and (now - _contact_cache["last_update"] < _contact_cache["ttl"]):
        return _contact_cache["data"]

    try:
        r = requests.post(
            f"{API_URL}/chat/findContacts/{INSTANCE}",
            headers=HEADERS,
            json={"where": {}},
            timeout=20
        )
        if r.ok:
            data = r.json()
            _contact_cache["data"] = data
            _contact_cache["last_update"] = now
            # print(f"♻️ Contactos actualizados ({len(data)})")
            return data
        else:
            print("⚠️ Error al obtener contactos:", r.status_code)
            return _contact_cache["data"]
    except Exception as e:
        print("❌ Error en conexión con Evolution:", e)
        return _contact_cache["data"]


def normalizar_jid(jid, push_name=None):
    """
    Convierte un JID '@lid' a '@s.whatsapp.net' usando:
    1️⃣ pushName
    2️⃣ profilePicUrl parcial
    3️⃣ coincidencia por ID corto
    """
    if not jid.endswith("@lid"):
        return jid

    contactos = find_all_contacts()
    if not contactos:
        print("⚠️ No se encontraron contactos en Evolution.")
        return jid

    # 1️⃣ Coincidencia exacta o parcial por nombre
    if push_name:
        for c in contactos:
            name = str(c.get("pushName", "")).lower()
            if push_name.lower() in name and c["remoteJid"].endswith("@s.whatsapp.net"):
                print(
                    f"🎯 Coincidencia por nombre: {push_name} → {c['remoteJid']}")
                return c["remoteJid"]

    # 2️⃣ Coincidencia parcial en la foto
    for c in contactos:
        url = c.get("profilePicUrl", "")
        if url and "whatsapp.net" in url and c["remoteJid"].endswith("@s.whatsapp.net"):
            #if any(k in url for k in ["310312407_150486224367959"]):
            if any(k in url for k in ["-"]):
                # print(f"🎯 Coincidencia por foto: {url} → {c['remoteJid']}")
                return c["remoteJid"]

    # 3️⃣ Coincidencia por ID parcial
    short = jid.split("@")[0][-5:]
    for c in contactos:
        if short in c["remoteJid"] and c["remoteJid"].endswith("@s.whatsapp.net"):
            print(f"🎯 Coincidencia por ID parcial: {short} → {c['remoteJid']}")
            return c["remoteJid"]

    print("⚠️ No se encontró coincidencia para:", jid)
    return jid


# --- 🔎 Ejemplo de uso ---


def returndata(webhook):

    jid_original = webhook["key"]["remoteJid"]
    push_name = webhook.get("pushName")
    id_resuelto = normalizar_jid(jid_original, push_name)

    return {
        "uidbasic": jid_original,
        "remoteID": id_resuelto
    }

# return (data)  # Convierte el diccionario a una cadena JSON


def imprimirresultado():
    webhook = {
        "key": {"remoteJid": "268113450905721@lid"},
        "pushName": "< David />",
        # "message": {"conversation": "Hola ia que tal"}
    }

    jid_original = webhook["key"]["remoteJid"]
    push_name = webhook.get("pushName")
    id_resuelto = normalizar_jid(jid_original, push_name)

    print("🔍 JID ORIGINAL:", jid_original)
    print("✅ JID NORMALIZADO:", id_resuelto)
    print("👥 Total contactos (en caché):", len(find_all_contacts()))


#imprimirresultado()

webhook = {
    "key": {"remoteJid": "131142682415195@lid"},
    "pushName": "Mama",
    # "message": {"conversation": "Hola ia que tal"}
}
# print(returndata(webhook)["uidbasic"])
# print(returndata(webhook)["remoteID"])
