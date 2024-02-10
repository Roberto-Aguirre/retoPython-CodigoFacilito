#Tuplas - Diccionarios


############## Indices
# settings = ("localhost",3306,"root","password","database")

# # print(settings[1:])

# tuples = (
#     {1, 2, 3},
#     {4, 5, 6},
#     [7, 8, 9]

# )

# for number1,number2,number3 in tuples:
#     print(number1,number2,number3)




############# DICCIONARIOS 
user = {
    "name": "Cody",
    "age": 10,
    "email":"info@cody.com",
    "active": True,
    #Elementos dentro de la tupla
    10:3.14,
    True:"Verdadero",
    #Tupla dentro de una diccionario
    (1,2,3): "Tuple"
}

# print(user)
# Class <dict>
# print(type(user))
# Imprimir el valor del elemento
# print(user["active"])
# print(user[(1,2,3)])

#Control sobre el diccionario
# if "username" in user:
#     print(user["username"])
# else:
#     print("Ese elemento no existe")

# # # # Mejor forma de escribrilo
#None -> Nada
    #metodo Get para obtener informacion
    #No usar [""], porque dara error
    # dict.get("propiedad/llave","caso default")
# value = user.get("username","No existe la llave")
# print(value)

#### key, value, item
        ## List and tuple
print(
    # user.keys(),
    # user.values()
    #Solo se puede usar el metodo .values una vez

    # tuple(user.values())
    # list(user.values())
    #tupla o lista de las llaves
    # list(user.keys())
    # tuple(user.keys())
    

)
##### items
# print(user.items())

### propiedades de la tupla
# for key,value in tuple(user.items()):
#     print(key,value)

user["age"] = 20
print(user["age"])
