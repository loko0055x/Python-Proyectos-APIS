arreglo = [['Arazely', '12'], ['David', '12'], ['Lucero', '12'], ['Jennifer', '20']]

# Convertimos edad a entero para comparación correcta
resultado = min(arreglo, key=lambda x: (int(x[1]), x[0]))

print(resultado)