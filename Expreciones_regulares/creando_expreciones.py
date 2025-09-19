
import re 

#detectando un numero CABA y ocultado
texto="Hola pedro mi numero es : +54 11 4321-4321"

#tiene que iniciar con un +
pattern=r'\+\d{2}\s' 
pattern=r'\+\d{1,3}\s\d{2}\s\d{4}-\d{4}' 


#remplazar por
remplazo = re.sub(pattern,"(Numero oculto)",texto)

print(remplazo)