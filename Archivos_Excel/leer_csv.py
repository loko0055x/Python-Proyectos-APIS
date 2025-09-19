
import csv

with open("Archivos_Excel\\Datos.csv") as archivo:
    reader=csv.reader(archivo)
    for row in  reader :
        print(row)