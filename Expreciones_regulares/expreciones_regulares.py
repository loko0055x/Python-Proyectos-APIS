#importamos re que es el modulo que se usa para trabajar con expreciones regulares
#es el que mas que se usa re
import re

texto= """Hola maestro, esta es la cadena 1. como estas mi capitan.
Esta es la   linea 2 de texto. 
y esta es la final. bbita (linea 3) 322 agg definitiva mi capitan"""

#buscare hola en la variable texto
result=re.search("maestro",texto)
#result te imprime o te dice en que posicion lo encontro

#3er parametro es = modificadores que alteran el comportamiento de la búsqueda
#findall = busque todo  los esta
#result=re.findall("esta",texto,flags=re.IGNORECASE)


# \d --> Busca digitos Numericos del 0 - 9

#r = lo voya decir que voya usar expreciones regulares
#busca los algun numero del 0 - 9 en la variable texto
result=re.findall(r"\d",texto)

# \D --> Busca todo menos digitos numericos o menos numeros
result=re.findall(r"\D",texto)


# \w --> Busca caracteres alfanumericos [a-z A-Z 0-9 _]  =
# _ GUION Bajo en python se considera alfanumerico
result=re.findall(r"\w",texto)


# \w --> Busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _]  =
result=re.findall(r"\W",texto)

# \s --> Busca espacios en blanco -> espacios ,tabs, saltos de linea 
result=re.findall(r"\s",texto)

# \S --> TODO MENOS Busca espacios en blanco  
result=re.findall(r"\S",texto)

# \. --> TODO MENOS SALTOS de linea
result=re.findall(r".",texto)

# \n --> Todos los saltos de linea
result=re.findall(r"\n",texto)

# \ --> Cancelar caracteres especiales
# caracteres especiales son todos los que no son alfanumericos
#es como decir buscame solo los puntos del texto
result=re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un PUNTO, seguido  un espacio
result= re.findall(r"\d\.\s",texto)

#buscando el principío de una linea 
# ^ = Busca el comienzo de una linea
#en el principio de una linea hay Hola  
#solo en la primera linea va a evaluar
#pero si colomamos en el tercer argumento  "re.M"
#significa multilinea
#re.M = Activa la multilinea
result=re.findall(r"^Esta",texto,re.M)

# $ = Busca el final de una linea
result=re.findall(r"capitan$",texto,re.M)

#{n} = busca n cantidad de veces el valor
# d -> numeros 
# si encuentra  3 digitos(numeros) juntos
# buscame 3 numeros juntos y seguido de un espacio
result=re.findall(r"\d{3}\s",texto)


#COINCIDENCIAS
#por lo menos q haya 1 coincidencias y maximo 4
#si hay entre 1 digito o 4digitos mostrame

result=re.findall(r"\d{1,4}",texto)


#conjuntos
#encuentra ab en ese orden
# la palabra tiene que contener una a seguido una b repetida entre (2-4)
# ab{2,4} -> la palabra (b) tiene que repetirse entre 2 o 4 veces
result=re.findall(r"ab{2,4}",texto)


# se tiene que repetir (ab) en una palabra entre 2 a 4 veces como maximo
result=re.findall(r"(ab){2,4}",texto)

# una palabra que contenga a y b que seaa seguido osea
# una palabra que tenga entre 2-4 la palabra -> a o b (tiene que estar seguido pero)
result=re.findall(r"[ab]{2,4}",texto)


# |  =  busca una cosa o la otra 
# | = or    o
# y si los  2 cumplen los 2 muestran
result=re.findall(r"\d{1,4}|Hola",texto)


print(result)
