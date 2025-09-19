diccionario={
    "name" : "Glen",
    "age":14
}
#Devuelve todas las key en una lista
result=diccionario.keys();

#Get = devuelve el valor segun su key  caso contrario retorna NONE
result=diccionario.get("age");

#Pop elimina un elemento de la lista con su key
result=diccionario.pop("name")

#obteniendo un elemento dict_items iterable
result=diccionario.items();
print(result)