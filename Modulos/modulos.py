#Si solamente quiero importar la funcion de un modulo 
from  modulos_saludar import  saludar,saludar_raro
from  modulos_saludar import  saludar as salu1,saludar_raro as salu2

import modulos_saludar  #as  m_s  

#Importar desde otro archivo .py

#data= m_s.saludar("Jan");
saludo=modulos_saludar.saludar("Jan") 
saludo=saludar("Jose")
print(saludo)
saludo=saludar_raro("Jose")
print(saludo)