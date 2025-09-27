import requests
import json
# URL de login
url = "https://app.xentrics.ai/invoices/operations/issue-invoice-v2"

headers = {
    "Accept": "text/x-component",
    "Content-Type": "text/plain;charset=UTF-8",
    "Cookie": "token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JhY2tlbmQueGVudHJpY3MuYWkvYXBpL2xvZ2luIiwiaWF0IjoxNzU4ODU4MjczLCJleHAiOjE3NTg5NDQ2NzMsIm5iZiI6MTc1ODg1ODI3MywianRpIjoiNFpLSDhjTWlzc243bUxUMSIsInN1YiI6Ijc0NiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.l9K94urSDYRQKYkIJA1ivc99Hsv86qaLd5mYYBTQuE4; company_id=2131",
    "Next-Action": "c170aa1ac624d4f62fd8e16a1fcf7a3adc3434d5",  # es muy importante
    "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(dashboard)%22%2C%7B%22children%22%3A%5B%22invoices%22%2C%7B%22children%22%3A%5B%22operations%22%2C%7B%22children%22%3A%5B%22issue-receipt-v2%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Finvoices%2Foperations%2Fissue-receipt-v2%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D"
}

payload = '[{"numero":"77485004","tipo":"dni"}]'
payload = '[{"numero":"20558124548","tipo":"ruc"}]'

# Enviar la solicitud POST
response = requests.post(url, headers=headers, data=payload)

# ------------------------------
# Extraer token y company_id
# ------------------------------

parsed_body = {}
lines = response.text.strip().splitlines()

for line in lines:
    try:
        key, raw_value = line.split(":", 1)
        value = json.loads(raw_value)

        # Si es key "0", la guardamos aparte como 'key_0'
        if key.strip() == "0":
            parsed_body["key_0"] = value
        # Si es key "1", unimos directamente los datos
        elif key.strip() == "1" and isinstance(value, dict):
            parsed_body.update(value)
    except Exception as e:
        print(f"\n[Error al parsear la línea]: {line}\n{e}")

# Imprimir el cuerpo combinado
print(json.dumps(parsed_body, indent=4, ensure_ascii=False))
