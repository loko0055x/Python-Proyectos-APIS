
import re
text = "Este es un ejemplo de una página web: https://www.example.com y también podemos vis"
#Siempre tiene que empezar con https 
#si encontras https en adelante mostramelo

pattern="https?://[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
 
result = re.findall (pattern, text)
print(result)


# * = 0 coincidencia o algunas
# + = al menos una coincidencia