#sumar numeros de mala forma
def sumar(arreglo):     
  var=0     
  for num in arreglo:
    var+=num   
    
  return var

# Utilizando el parametro args 
# SI CREAS UN PARAMETRO ARGS tiene que ser el ultimo parametro de tu funcion
#sumar de forma optima
#  *arreglo= le decimos exactamente que el argumento que enviemos 
#            se convierta en lista 
#osea nosotros podemos mandar como infinidad de ARGUMENTOS 
def sumarOptimo(name,*arreglo):     
      
   
  return f"Hola {name} su resultado es : {sum(arreglo)}"

print(sumarOptimo("David",5,6,6,8))