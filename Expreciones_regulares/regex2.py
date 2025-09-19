import re

# La cadena en la que se buscarán los patrones
text = "La fecha es 23/06/2021 у el teléfono es +1-555-555-5555"

# El patrón a buscar (2 digitos/2 digitos/4 digitos)

pattern = r"\d{2}/\d{2}/\d{4}"
# El texto con el que se reemplazará el patrón
replacement = "Fecha oculta"

# Reemplazar todas las apariciones del patrón en la cadena de texto 
#encuentra la cadena y hace un remplazo

#1er argumento -> el patron 
#2do argumento -> remplazar por esta cadena
#3er argumento -> la variable que se va a evaluar para remplazar

new_text = re.sub(pattern, replacement, text)
#new_text = ya tiene el texto modificado caso contrario no modifica el texto

# Imprimir el resultado
print("Texto modificado: ", new_text)