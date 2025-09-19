import re

text = "remplazando todas las vocales por el asterisco"

#pattern = mi metodologia

pattern = r"a|e|i|o|u"
replacement = "*"


new_text = re.sub("[aeiou]", "* ", text)

# Imprimir el resultado
print( new_text)