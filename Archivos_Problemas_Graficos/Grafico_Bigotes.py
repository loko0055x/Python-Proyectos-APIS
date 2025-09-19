import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df= pd.read_csv("Archivos_Problemas_Graficos\\bigotes.csv")


#scatterplot = Grafico de dispercion
sns.boxplot(x="categoria",y="valor",data=df)




#mostrando 
plt.show()
