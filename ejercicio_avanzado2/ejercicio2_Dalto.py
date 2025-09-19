#primos_hasta= lambda num :list(filter(lambda x : all (x% i !=0 for i in range(2, int(x**0.5)+1)),range(2,num)))
#print(primos_hasta(100))


def  es_primo(num) :
    for i in range(2,num-1) :
        if num%i==0 :
            return False
    return True
     


 
def primos_hasta (num) :
 arreglo=[]     
 for i in range (num) :
    result= es_primo(i)
    if result==True :
      arreglo.append(i)
 return arreglo


resultado= primos_hasta(13)
print((resultado))