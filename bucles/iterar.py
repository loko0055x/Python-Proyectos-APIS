animales=["perro","gato","cocodrilo","loro"]
edades=[5,10,2,3]
#usando un bucle for tradicional (NO FUNCIONA USANDO CONJUNTOS SET)
for i in range(len(animales)):
    print(animales[i])

#forma correcta de hacer un for traicional
#Retorna una tupla donde su key por asi decirlo es  el indice 
#es como te retorna una matriz por asi decirle 
 
for datos in enumerate(animales):
    index=datos[0]
    value=datos[1]
    print(f"el indice es {index} y su valor es {value}")
     

#usando un bucle foreach
for animal in animales:
    print(animal)    


print("-----------------------------------")

#como usar un foreach pero en una matriz ITERAR 2 LISTAS
for num,animal in zip(animales,edades):
    print(f"{num}  - {animal}")

#for else
for i in range( 5):
    print(i)
else:
    print("siempre se ejecutara el Else SIEMPRE")