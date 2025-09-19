import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df= pd.read_csv("Archivos_Problemas_Graficos\\dispercion.csv")


#scatterplot = Grafico de dispercion
sns.scatterplot(x="tiempo",y="dinero",data=df)





#mostrando 
plt.show()
