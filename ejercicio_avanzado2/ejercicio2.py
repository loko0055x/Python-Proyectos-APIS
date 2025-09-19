

nelementos= int(input("Digite un Numero : "))

numero=nelementos

estado=False


for i in range(1,numero)  :
      estado=False
      for j in range(2,i+1):
        resultado= i/j
        if(i%j==0):
          if(resultado==1 or  resultado==i):
           estado=True
          else:
           estado=False
           break    
      if estado:
       print(i)
 