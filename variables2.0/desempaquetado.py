#creando TUPLAS
arreglo= (["Lucas","Datos"]);


#desempaquetado
name,lastname=arreglo;

#creando tuplas de forma bien con tuples

arrtuplas= tuple(["dato1" ,"dato2"])

#otra forma de crear tuplas 
arrtuplas= "dato1","dato2"

#otra forma de crear una tupla con un solo elemento
arrtuplas= "dato1",

#creando CONJUNTOS SET
arreglo= set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto 
#frozenset = permite meter un conjutno de otro conjunto 
arreglo= frozenset (["dato1","dato2"])

arreglo={arreglo,"dato3"}
print(type(arreglo))

#