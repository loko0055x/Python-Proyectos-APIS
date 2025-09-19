import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df= pd.read_csv("Archivos_Problemas_Graficos\\pedex.csv")


#x="fecha" → el eje X toma los valores de la columna "fecha" del DataFrame df.
#y="pedexx" → el eje Y toma los valores de la columna "pedexx" del DataFrame df.
#data=df → le indicas a Seaborn que los datos están en el DataFrame df.

#sns.lineplot(...) → prepara el gráfico.
#plt.show() → lo muestra en pantalla.
#No necesitas pasarle el gráfico a plt.show()
#porque ya fue registrado dentro de matplotli
sns.lineplot(x="fecha",y="pedexx",data=df)

#especifiamos en que valor x,y si coinciden que se coloque un punto 
#creando un punto en el momento o dia que se cago mas xD 


#"01-09" → eje X (por ejemplo, una fecha).
#17 → eje Y (el valor a graficar).
#"o" → formato del punto, es decir, dibuja un marcador en forma de círculo.

plt.plot("01-09",17,"o")

 

plt.show()
