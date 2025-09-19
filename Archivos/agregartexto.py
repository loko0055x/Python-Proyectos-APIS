

#ahora le daremos el permiso de agregando
#esto es para agregar sin modificar los cambios anteriores 
#agrega correctemente 



with open("Archivos\\texto_dalto.txt",'a',encoding="utf-8") as archivo:
     
  #usando un bucle para agregar varias lineas 
  
 



   for i in range(5):
     archivo.write(f"Linea  {i+1} agregada\n")    

#with open("Archivos\\texto_dalto.txt", 'a', encoding="utf-8") as archivo: [archivo.write(f"Linea {i+1} agregada\n") for i in range(5)]
