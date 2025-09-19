#creamos una clase y hereda de exception
class MiException(Exception): 
    
    #constructor 
    def __init__(self, error):
         print(f"Impresionante cometiste elprimer error  {error}")
         
#raise MiException("que bld error ")         

try : 
  #aproposito generamos una exception
  raise MiException("que bld error ")

except:
    print("dsa")