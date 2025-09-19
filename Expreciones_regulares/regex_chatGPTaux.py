import re

texto = "Hola esto es una prueba que termina en 123 juax juax"
x = re.search(r"Hola.*123", texto)

if x:
    print("Coincide:", x.group())
else:
    print("No coincide")
