FILE_PATH = "Archivos\\textodemo.txt"
ENCODING = "UTF-8"




def add_people(name,lastname,age):
    with  open(FILE_PATH,"a",encoding=ENCODING) as archivo:     
      archivo.write(f"{getlastindex()+1},{name},{lastname},{age}\n");


def getlastindex(): 
    arreglo = abrir_archivo()
    if len(arreglo)==0 :
      return 0
    
    return int(arreglo[-1][0]);


def view_All():
    arreglo = abrir_archivo()
    print("#################################################")
    print(f"{'NOMBRE'.ljust(12)} - {'APELLIDO'.ljust(15)} - {'EDAD'}")
    print("-------------------------------------------------")
    i=1
    for persona in arreglo:
        
        nombre = persona[0].ljust(12)
        apellido = persona[1].ljust(15)
        edad = persona[2]  # Asegúrate que sea string si no lo es
        print(f"{i}) {nombre} - {apellido} - {edad}")
    print("#################################################")

def delete_for_id(pos): 
    with open(FILE_PATH,'r',encoding=ENCODING) as archivo:
      lineas = archivo.readlines()
      lineas[pos] = ""
    with open(FILE_PATH, 'w', encoding=ENCODING) as archivo:
     archivo.writelines(lineas)


def update_for_id(pos,id,name,lastname,age): 
    with open(FILE_PATH,'r',encoding=ENCODING) as archivo:
      lineas = archivo.readlines()
      lineas[pos] = f"{id},{name},{lastname},{age}\n"

    with open(FILE_PATH, 'w', encoding=ENCODING) as archivo:
     archivo.writelines(lineas)



def search_for_id(id):
  arreglo= abrir_archivo()
  return list(filter(lambda x: x[0] == id, arreglo))




#tengo que darle permisos de read leer
def abrir_archivo():
    arreglo=[]
    with  open(FILE_PATH,"r",encoding=ENCODING) as archivo:
     data = archivo.readlines();
     for i in range(0,len(data)) :
      
      persona_arr= data[i].split(",")
      tupla= tuple([persona_arr[0],persona_arr[1],persona_arr[2],persona_arr[3]])
      arreglo.append(tupla)
      
    return arreglo
 
 



def getpositionfor_Id(id):
 arreglo= abrir_archivo()
 for i in range(0,len(arreglo)) :  
    if id==arreglo[i][0]:
     return i

 return -1





print("################################################")
print("Bienvenido al crud de not de blotas")

while(True) : 
    
        print("-------------------------MENU-------------------------")
        print("1) Ver Lista ")
        print("2) Agregar Persona ")
        print("3) Actualizar Persona")
        print("4) Eliminar Persona ")
        print("5) Buscar Persona")
        print("6) Salir ")
        opcion = int(input("Ingresa una opción (1 o 6): "))

        match opcion:
         case 1:
          view_All()
         case 2:
          print("Elegiste opción 2")
          name=input("Escriba nombre : ")
          lastname=input("Escriba apellido : ")
          age=input("Digite  edad : " )
          add_people(name=name,lastname=lastname,age=age)
         case 3:
          print("Elegiste opción 3")
          id=input("Digite el id que desea actualizar : ")
          pos=getpositionfor_Id(id)
          if(pos==-1):
            print("No Existe el ID")
          else :
           name=input("Escriba nombre : ")
           lastname=input("Escriba apellido : ")
           age=input("Digite  edad : ")
           update_for_id(pos,id,name,lastname,age)
         case 4:
          print("Elegiste opción 4")
          id=input("Digite el id que desea Eliminar : ")
          pos=getpositionfor_Id(id)
          if(pos==-1):
            print("No Existe el ID")
          else :
           delete_for_id(pos=pos)
         case 5:
          print("Elegiste opción 5")
          id=input("Digite el id que desea vizualizar : ")
          pos=getpositionfor_Id(id)
          if(pos==-1):
            print("No Existe el ID")
          else :
           print(search_for_id(id))
          
         case _: 
          print("Gracias por usar el programa")
          break;

 



 