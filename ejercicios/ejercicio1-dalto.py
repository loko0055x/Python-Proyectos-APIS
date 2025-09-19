horadalto=1.5
horamin=2.5
horaprom=4
horamax=7

crudo_promedio=5
crudo_dalto=3.5

#calculos de primero ejercicio
diferencia_con_min= 100 -  (horadalto/horamin*100)
diferencia_con_max= 100 -  (horadalto*1000//horamax/10) #NUEVA FORMULA DE OBTENER SIN TANTOS DECIMALES
diferencia_con_promedio= 100 -  (horadalto/horaprom*100)

#calculando  el porcentaje de tiempo vacio 
tiempo_vaciopromedio=100- (horaprom/crudo_promedio*100)
tiempo_vaciodalto=100- (horadalto/crudo_dalto*100)

#calculando el tercer ejercicio
resultado1=(horaprom*10/horadalto)
#resultado1=(horaprom*100//horadalto/10)
resultado2=(horadalto*10/horaprom)

#ejercicio 1

#print(f"El curso de dalto dura  {diferencia_con_min}%   menos que el mas rapido")
#print(f"El curso python dalto lo explico mas rapido en un  {diferencia_con_min}%  ")
print("-----------------------------------------")
print(f"El curso de dalto dura  un {diferencia_con_min}%   menos que el mas rapido")
print(f"El curso de dalto dura  un {diferencia_con_max}%   menos que el mas lento")
print(f"El curso de dalto dura  un {diferencia_con_promedio}%   menos que el promedio    ")


print("-----------------------------------------")
print(f"El curso promedio elimina un {tiempo_vaciopromedio}%  de tiempo vacio")
print(f"Este curso elimino el {tiempo_vaciodalto}%  de tiempo vacio")


print("-----------------------------------------")
print(f"Ver 10 horas de este curso equivale a ver {resultado1} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {resultado2 } horas de otros cursos")
 