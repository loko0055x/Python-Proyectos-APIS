
#codificacion UTF -8 
# es una codificacion universal que lee todos los caracteres
#usando OPEN PARA ABRIR UN ARCHIVO
archivo_sin_leer = open("archivos\\texto_dalto.txt",encoding="UTF-8")
#archivo=archivo_sin_leer.read()
#leer el archivo 

#leer las lineas y almacenar en un arreglo 
#lineas_all=archivo_sin_leer.readlines()

#LEER la primera linea del texto
linea=archivo_sin_leer.readline();


archivo_sin_leer.close()

print(linea)