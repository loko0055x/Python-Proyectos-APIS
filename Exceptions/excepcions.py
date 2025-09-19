def suma():
 
 while(True) :
  a =(input("Numero 1 : "))
  b=(input("Numero 2 : "))
  try :
    result=int(a)+ int(b)  
  except Exception as e: 
    print(f"ERROR DE NUMEROS {e}")
    print(f"Nombre de la excétion {type(e)}")
    print(f"Nombre de la excétion {type(e).__name__}")

  else :
    # Se ejecuta solo si **NO hay error**
    break
  finally :
    print("Manejo de exception finalizado")

 return result

print(suma())