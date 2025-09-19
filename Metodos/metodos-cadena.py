cadena1="hola soy david y el agua es vida"
cadena2="juego dota 2"
  
#Funciones de python 

#dir =este metodo me da una lista de metodos que puede tener esa variable 
result_dir=dir(cadena1)

 
#ESTO ES UN METODO POR QUE TIENE EL nombre de una variable luego un punto donde puede acceder 
#a cualquier metodo 
#METODO =  Dato  . metodo  () =  Estructura correcta   OOOOJOOOOOOOOOOOOOOO
#Upper  = convierte todo mayuscula
resultado= cadena1.upper();

 

#Lower  = convierte todo mayuscula
resultado=cadena1.lower()
 

#CAPITALIZE = conviertetodo en minuscula excepto la primera letra 
resultado=cadena2.capitalize()


#Find = buscar una cadena en otra cadena
#Encuentra la cadena y te retorna en que posicion esta caso contrario retorna -1
resultado=cadena1.find("a")

#Index =es lo mismo que find la diferencia es que retorna una exception si no encuentra el indice
resultado=cadena1.index("a")

#ISNUMERIC = si una variable es numero retorna true caso contrario false 
resultado= "5".isnumeric()
 
#ISALPHA = si una variable es alfanumerico(caracter y numeros) ESPACIO NO CUENTA Y  retorna true caso contrario false
resultado= "5as".isnumeric()

#COUNT = en una cadena cuantas veces se repite una letra , caso contrario retorna  0
resultado=cadena1.count("av")

#LEN = longitud de una cadena
resultado=cadena2.__len__();

#startswith = empieza una cadena en ?
resultado=cadena1.startswith("h");

#endswith = termina en una cadena en ?
resultado=cadena1.endswith("a");

#replace 
#remplaza una cadena  con una cadena nueva 2parametros
#1er - la cadena antigua que quiero remplazar
#2da - la cadena nueva por la que quiero que se remplaze
resultado=cadena2.replace("juego","disfruto")
 
#split 
resultado=cadena1.split(" ")
 
