#por convencion se pone pd 
import pandas as pd 


#le ponemos como variable df
#por que hace representacion al "Data Frame"
# son estructuras de datos bidimencionales similares a una hoja de calculo
#especificamos como podemos acceder alo que querramos
#al colocar names= estamos diciendo que seria como nuestro encabezado
#df= pd.read_csv("Archivos_Excel\\Datos.csv",names=["name","lastname","age"])
df= pd.read_csv("Archivos_Excel\\Datos.csv")
df2= pd.read_csv("Archivos_Excel\\Datos.csv")

#obteniendo los datos de la columna 
nombre=df["nombre"]

#ordenando dataframe por la edad
df_ordenado_ascendente=df.sort_values("edad")

#ordenandolo de forma descendente X defecto viene coomo ascendente de menor a mayor
#false= para negar por asi decirlo 
df_ordenado_descentente=df.sort_values("edad",ascending=False)


#concatenando los 2  dataframes
dfconcatenado=pd.concat([df,df2])


#accediendo alas 3 primeras filas  con head()
#te muestra que cantidad de filas queres que se muestre 
#HEAD= accedemos ala inf de arriba hacia abajo

primeras_fila= df.head(3)

#accediendo alas 3 ultimas filas  con tail()
#TAIL= accedemos ala inf de abajo hacia arriba
ultimas_fila= df.tail(3)




#accediendo ala cantidad de filas y columnas  con SHAPE
filas_y_columnas_totales =df.shape


#desempaquetado
cant_filas,cant_columnas=df.shape


#cant_filas=filas_y_columnas_totales[0]
#cant_columnas=filas_y_columnas_totales[1]

# muestra (filas,columnas)


#obteniendo datas estadistica del dataframe  sirve para analisis de datos
df_info=df.describe()



#-----------------------------  Slicing   -----------------------------#
 
#accediendo a un elemento especifico  del data frame con  LOC
# es como una matriz 
# 1er Indice que deseamos acceder
# 2do el valor (KEY) que queremos que se muestre
elemento_especifico_loc=df.loc[2,"edad"]


#accediendo a un elemento especifico  del data frame con  ILOC
#AHORA ES por indices el iloc
#es por indices es como una matriz 
# 1er Fila
# 2do Columna
elemento_especifico_Iloc=df.iloc[2,2]


#accediendo a todas las filas de una columna 
#la , va por que ILOC funciona asi iloc[filas, columnas]
apellidos= df.iloc[:,1]

#accediendo ala fila 3 con loc
#fila_3=df.loc[2,:] 
fila_3=df.loc[2,:] 

#accediendo ala fila 3 con Iloc
fila_3=df.iloc[2,:] 

#accediendo a filas con edad mayor a 30
mayor_que_30=df.loc[df["edad"]>30,:]

print(mayor_que_30)
