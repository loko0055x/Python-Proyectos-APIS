
#teoria de conjuntos
conjunto1={1,3,5,7}
conjunto2={1,3,7}

#verificar si un conjunto es un subconjunto de otro
#conjunto2 es un sub conjunto de conjunto 1
#osea en Conjunto 1 podemos encontrar algunso elementos del conjunto 2
#retorna true si es correcto 
result=conjunto2.issubset(conjunto1)

result=conjunto2 <= conjunto1

#verificamos si es un super conjunto
# el conjunto 1  es un super conjunto de conjunto 2
result=conjunto1.issuperset(conjunto2)
result= conjunto1 > conjunto2

#verificar si hay algun numero en comun de 2 conjuntos o listas
#retorna true si existe algun numero repitente entre las listas 
result=conjunto2.isdisjoint(conjunto1)
print(result)
