compañeros=[];

compañeros.append(("Jennifer    ",11))
compañeros.append(("Arazeli",11))
compañeros.append(("Lucero",11))
compañeros.append(("David",18))

#forma de que gracias a dalto resolvi

#lista=sorted(compañeros)
#minimo=min(list(map(lambda x :x[1],compañeros)))
#print(list(filter(lambda x : x[1]==minimo,lista))[0])


compañeros.sort(key=lambda x : x[1])

asistente=compañeros[0][0]
profesor=compañeros[-1][0]
print(f"El assitente  es {asistente} y el profe es {profesor} ")