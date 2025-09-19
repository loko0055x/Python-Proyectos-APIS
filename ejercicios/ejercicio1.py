horadalto=1.5
horamin=2.5
horaprom=4
horamax=7
crudodalto=3.5
crudopromedio=5
print("--------------------------------------------")


#ejercicio 1
result=horadalto/horamin*100
#result=100-result;
print(f"el más rapido de otros cursos en porcentaje es :  {result} %") 

result=horadalto/horamax*100
#result=100-result;

print(f"el más lento de otros cursos en porcentaje es :  {result}%") 
result=horadalto/horaprom*100
#result=100-result;

print(f"el promedio de los cursos en porcentaje es :  {result}%") 

#ejercicio 2
print("--------------------------------------------")
 
result=horaprom/crudopromedio*100
print(f"En el promedio se redujo en  :  {result}%") 
result=horadalto/crudodalto*100
print(f"En dalto se redujo en  :  {result} %") 


#ejercicio 3
print("--------------------------------------------")

multi = horadalto*10 # 25
result=multi//horaprom

print(f"10 horas de curso  equivale a   :  {result}") 

multi = horaprom*10 # 40
result=multi//horadalto
print(f"10 horas de curso  equivale a   :  {result}") 