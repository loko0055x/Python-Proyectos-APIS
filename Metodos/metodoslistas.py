#creadno una lista con list()
lista= list(["Glen","david"])

#agregando elementos ala lista
#append = agrega defrente un elemento ala lista de forma ordenada
lista.append("Lucero")

#extend = agregando un elemento ala lista en un indice especifico
lista.insert(0,"Jose")
 
#extend = agregar varios elementos ala lista
lista.extend(["Juan","Leonardo"])

#pop = elimina un elemento de la lista segun su indice
lista.pop(0);
lista.pop(-1) #ELIMINA EL Ultimo elemento de la lista (Sucesivamente penultimo, antepenultimo)

#remove = remueve un elemento de la lista por su valor caso contrario lanza excepcion 
lista.remove("david") 
 
#clear = elimina todos los elemetos de la lista
#lista.remove();

#short = ordena de forma ascendente
lista.sort();
#short = ordena de forma INVERSA osea al contrario
lista.sort(reverse=True);

#reversa = revierte  la lista del primero al ultimo sucesivamente
lista.reverse();
print(lista.index("Glen")) 