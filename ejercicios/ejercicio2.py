#ejercicio 1
promedio =1;

cadena= input("Escriba una frase  :\n")

arr=cadena.split(" ");
longitud=len(arr)

second= longitud/2;
print(f"El usuario al decir la frase '{cadena}' tardo {second}  segundos ")
print(f"El usuario dijo  {longitud}  palabras ")

if(second>60):
       print("Pára flaco tampoco te pido un testamento " )


milisegundo = 1000; #= 1 segundo

#Cual es el 130 de 1000
milisegundo_dalto = 1000 / 100 * 130;
segnormal = milisegundo / 1000.0;
 #dalto habla esto 
segdalto = milisegundo / milisegundo_dalto;

print(f"los segundos que habla una personal normal  :{segnormal}");
print("los segundos que habla dalto                : {segdalto}");
print("--------------------------");

#cantidad de palabras  / cantidad de milisegundos 
# 500 milisegundo  = 1 palabras
#0.384 milisegundos = 1 palabras              
arreglo = cadena.split(" ");
cantpalabras = len(arreglo);

segundoxpalabra=segnormal/2;
segundoxpalabra_dalto=segdalto/2;
print(f"La cantidad de palabras es   : {cantpalabras}");
segnormal =cantpalabras*segundoxpalabra;
segdalto = cantpalabras*segundoxpalabra_dalto;
print(f"los segundos que se demora una personal normal es de : {segnormal} segundos" );
print(f"los segundos que se demora SOY DALTO ES DE           : {segdalto} segundos" );
 

resultadodalto=cantpalabras/2*1.3

print(f"Segun dalto son {resultadodalto} segundos")