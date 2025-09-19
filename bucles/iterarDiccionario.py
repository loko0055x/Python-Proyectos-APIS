json={
 "name" : "glen",
 "lastname" : "kt",
 "age" : 15

}

#imprimte todos los key y values
print(json.items()) 
#retorna todos los Keys
print(json.keys())
#retorna todos los values 
print(json.values()) 

print("---------------------------------------")

for data in json.items() :
    key=data[0]
    value=data[1]
    print(f"Key es  '{key}' el valor es '{value}'")
    

 