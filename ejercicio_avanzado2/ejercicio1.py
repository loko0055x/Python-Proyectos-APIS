#nombre=input("Escriba su nombre  : ")
#edad = input("Digite  su edad    : ")


#print(f"El nombre es {nombre} y su edad {edad}");



def pedirdatos(i):
    print("------------------")
    print("Desea agregar un estudiante")
    print("1) Si")
    print("2) No")
    estado=input("")
    if estado!="1":
     return -1
    print(f"Estudiante {i}")
    nombre=input("Escriba su nombre  : ")
    edad = input("Digite  su edad    : ")
    return nombre,edad



i=0

arreglo=set();
while(False):
    data=pedirdatos(i+1);
    if(data==-1):
       break;
    arreglo.add(data)


arreglo={ ('Jennifer', '11'),('Arazely', '11'), ('David', '17'),('Lucero', '11')}
arreglo=list(arreglo)



lambda1_py=lambda x: x[0] ;
lambda2_py=lambda x: x[1] 
filtrado_nombre = filter(lambda1_py, arreglo)
filtrados_edad = filter(lambda2_py, arreglo)


arreglo_nombre=list(map(lambda1_py,filtrado_nombre))
arreglo_edad=list(map(lambda2_py,filtrados_edad))


edadminima=min(arreglo_edad)
edadmaxima=max(arreglo_edad)

print(arreglo_edad)
print(arreglo_nombre)

lambda_min=lambda x : x=="11" 

print(list(filter(lambda_min,arreglo_edad)))

#funcion_lambda=lambda x : x[1] if
#print((f"{(arreglo[0][1])}"))


