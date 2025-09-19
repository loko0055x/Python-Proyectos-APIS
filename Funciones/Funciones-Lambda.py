
arreglo=[1,2,3,4,5,6,7,8,9]

#lambda es una forma  de crear funciones anonimas 
#podemos almacenar en variables 

multiplicar_por_2 = lambda x:  x*2

#creando una funcion comun si es par o no

def evaluarnum (num):
    if num %2==0 :    
     return True
    
#usar filter con una funcion comun
#el argumento enviado es como cada elemento del arreglo talcual 
#es como internamentte tiene un bucle 
#si es true lo agrega ala lista
numeros_pares = filter(evaluarnum,arreglo)
lista_par=list(numeros_pares)

 


#creando funcion para evaluar numeros pares con usando funcion lambda
numeropares_list_lambda = filter((lambda x:  x%2==0),arreglo) 
print(list(numeropares_list_lambda));
