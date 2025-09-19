
def fibonacci(num) :
    #Cuándo está bien declarar en líneas separadas?
    #Cuando las variables no dependen de otras variables 
    a=0
    b=1
    fibonacci_lista=[0]
    for i in range(num) :
        if a+b> num:
            return  fibonacci_lista 
        else :
          fibonacci_lista.append(b)
          a,b= b,a+b
        

resultado=fibonacci(20)
print(resultado)    