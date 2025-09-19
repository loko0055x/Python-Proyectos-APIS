

arreglo =[['Arazely','12'], ['David','11'], ['Lucero','12'], ['Jennifer','20']]
 
lamda_edad =lambda x : x[1]
arreglo_edades=list(map(lamda_edad,arreglo))
edadmenor= min(arreglo_edades)

arreglo_edades= list(filter(lambda x : x==edadmenor,arreglo_edades))



auxlistaname=list(filter(lambda x: x if x[1]==edadmenor else None ,arreglo))
nombre_bajo=min( list(map(lambda x : x[0],auxlistaname)))
print(list(filter(lambda x : x[0]==nombre_bajo and x[1]== edadmenor,arreglo )))


#print(list(map(lamda_edad,arreglo)))