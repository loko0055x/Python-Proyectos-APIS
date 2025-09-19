
diccionario = {
    "data": [
    {"name": "Jenifer", "edad": 4},
    {"name": "Glen David", "edad": 4},
    {"name": "Lucas Martínez", "edad": 7},
    {"name": "Ana Sofía", "edad": 6},
    {"name": "Mateo Ruiz", "edad": 5},
    {"name": "Camila Torres", "edad": 8},
    {"name": "Santiago López", "edad": 9},
    {"name": "Valentina Ríos", "edad": 5},
    {"name": "Emilia Fernández", "edad": 9},
    {"name": "Tomás Herrera", "edad": 5},
    {"name": "Isabella Castro", "edad": 4}
    ]
}
#obtener el elemento
#aux=diccionario.get("data")[0].get("name")

aux=diccionario.get("data")

#diccionario.get("data") = list

#diccionario.get("data")[0] = dict


#print(list(filter(lambda_cadena,lista_repetido)));

#print(list(filter(data_lambda, arreglo_edad)))


#print(f"La edad menor es {edad_menor} : de nombre {arreglo_nombre[indice]}")





############################################################################
arreglo_nombre  = list(map(lambda x: x["name"], aux))
arreglo_edad= list(map(lambda x: x["edad"], aux))
 
edad_menor= (min(arreglo_edad))
edad_mayor=(max(arreglo_edad))

indice=arreglo_edad.index(edad_menor)

# retornar las posiciones donde el valor sea 4 


combinado = list(zip(arreglo_nombre, arreglo_edad))
#print(combinado) #todos 
#print(combinado[0]) #  nombre y   edad juntos en uno solo 
#print(combinado[0][0]) # solo nombre
#print(combinado[0][1]) # solo edad

#print((combinado))

lambda_auxiliar1= lambda data: data[0] if data[1] == edad_menor else None

lambda_auxiliar2= lambda data: data[0] if data[1] == edad_mayor else None


#retorna todas elementos donde la edad sea menor
lista_repetido1=list(filter(lambda_auxiliar1,combinado));
#retorna todas elementos donde la edad sea mayor

lista_repetido2=list(filter(lambda_auxiliar2,combinado));
 


print(f"El menor (ASISTENTE) de todos es  {min(lista_repetido1)}")
print(f"El mayor (DELEGADO) de todos es  {max(lista_repetido2)}")



############################################################################







#print(dict(diccionario.get("data")))


#for data_key in aux:
  #print(data_key.get("name"))


data_lambda= lambda x : x.get("edad")==5

#print(aux)
#print(list(filter(data_lambda, aux)))








for data  in diccionario.get("data"):

    key= data.get("name")
    value= data.get("edad");
  
    #print(f" Nombre es  : {key},La edade es : {value}") 