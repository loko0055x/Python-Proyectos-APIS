
#ESto es como asginar un valor por defecto 
def frase (name,lastname,adjetivo="Tonto"):
   return f"Hola {name} {lastname} , sos muy {adjetivo}"

frase_result= frase( "David","KT")


print(frase_result)