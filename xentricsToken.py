import base64
import json

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JhY2tlbmQueGVudHJpY3MuYWkvYXBpL2xvZ2luIiwiaWF0IjoxNzU4ODU4MjczLCJleHAiOjE3NTg5NDQ2NzMsIm5iZiI6MTc1ODg1ODI3MywianRpIjoiNFpLSDhjTWlzc243bUxUMSIsInN1YiI6Ijc0NiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.l9K94urSDYRQKYkIJA1ivc99Hsv86qaLd5mYYBTQuE4"

# separar el token en sus 3 partes
header_b64, payload_b64, signature = token.split(".")

# función para decodificar base64


def b64decode(data):
    padding = '=' * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


payload = json.loads(b64decode(payload_b64))
print(json.dumps(payload, indent=2))
