import base64

# Ruta local de la imagen
ruta_imagen = "C:\\Users\\Usuario\\Downloads\\IMG_20241230_183552.jpg"
ruta_imagen = "C:\\Users\\Usuario\\Pictures\\comprobante.jpg"

# Leer la imagen y convertir a base64
with open(ruta_imagen, "rb") as f:
    base64_img = base64.b64encode(f.read()).decode("utf-8")

print("Base64 de la imagen:\n")
# print(base64_img[:500] + "...")
print(base64_img)
