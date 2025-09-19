import pandas as pd

df= pd.read_csv("Archivos_Problemas\\Datos.csv")

#cambiar el tipo de datos de una columna de entero a String 

#df["edad"]= df["edad"].astype(str)

#REMPLAZANDO los datos 
df["nombre"] = df["nombre"].replace(to_replace="Lucas", value="JOSEX")

#como eliminar datos o filas que estan incompletas
#eliminando filas con datos faltantes 
#si es que un dato o columna esta incompleto o ta VACIO se elimina la fila y no se muestra 

#axis 
#si queremos eliminar las columnas con datos faltantes 
#AXIX 
#df= df.dropna(axix=1)

#El parametro 0 = Columnas
#El parametro 1 = Filas
#como eliminar datos o filas que estan incompletas (datos faltantes)

df= df.dropna()


#eliminar las filas  duplicadas repetidas
df=df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("Archivos_Problemas\\Datos_Limpios.csv")

