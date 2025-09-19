
nombres=["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos=["Dalto","Zing","Dalto"," Rubetix","tarado"]


#Registrar esta informacion en un Txt de forma optima

with open("Archivos_Problemas\\problema.txt","w",encoding="UTF-8" ) as archivo :
   
   #realizando con una sola linea de codigo 
    archivo.writelines("Los Datos son : \n\n")
    [archivo.writelines(f"Nombre : {name} \nApelido : {lastname}\n------------------\n") for name,lastname in zip(nombres,apellidos)]
   

    #for name,lastname in zip(nombres,apellidos):
    #    archivo.write(f"{name},{lastname}\n")
        



