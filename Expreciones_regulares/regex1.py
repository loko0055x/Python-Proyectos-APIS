
import re
text = "The quick brown fox jumps over the lazy dog"
#buscame la cadena donde 
# The aparesca al principio


# .*   -> Coincidir con cualquier carácter
#         (excepto saltos de línea \n), incluidos los espacios en blanco.
x = re.search("^The.*dog$", text)

if x:
    print("SI")
else:
    print("NO")
