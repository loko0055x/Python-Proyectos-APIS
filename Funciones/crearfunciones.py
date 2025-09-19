#creando una funcion de contraseñas

def crear_contraseña_ramdon(num):
    listado='abcdefghijkl'
    numero_String =str(num) #convierte de numero a text
    # num= "10"
    num=int(numero_String[0])     # 1
    c1=num-2   #1-2
    c2=num     #1
    c3=num-5   #1-5
    print(listado[-12])
    contra=f"{listado[c1]}{listado[c2]}{listado[c3]}{num*2}"
    return (contra)

print(crear_contraseña_ramdon(99))