import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df= pd.read_csv("Archivos_Problemas_Graficos\\cofla_ingresos.csv")


#barplot = para grafico de barras  
sns.barplot(x="fuente",y="ingresos",data=df)



total_ingresos=df.get("ingresos").sum()
total_ingresos=df["ingresos"].sum()
 

print(f"El total de ingresos es $.{total_ingresos}") 
#mostrando 
plt.show()
