import base64
import json
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ..."
payload = token.split('.')[1]
# ajustar padding
payload += '=' * (-len(payload) % 4)
data = json.loads(base64.urlsafe_b64decode(payload).decode())
print(json.dumps(data, indent=2))
