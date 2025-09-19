#leeer archivos de una forma correcta en vez de estar abriendo y cerrando 

#forma optima de abrir un archivo sin necesidad de estar
#cerrando etc

#el segundo parametro de open 'w'
#le estamos diciendo que nos de permiso de ESCRITURA (Write)
#lo que hace es Sobre escribir el archivo 
with open("Archivos\\texto_dalto.txt",'w',encoding="utf-8") as archivo:
     
     #sobreescribiendo el archivo 
     #archivo.write("JAJAJAJ Te la recontre teclee")
     
     #Es lo mismo a diferencia que puedes poner una lista 
     #agregando 2 lineas
     archivo.writelines(["- Hola maestro como andas\n","- Misercordia\n"])    
     archivo.writelines(["- No se por que dijiste eso\n","- Yo tampoco"])