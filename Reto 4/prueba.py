
id = [1,2,3,4,5]
usuarios = [{"id":1}]

# id[1] = {
    # "id" : 1,
    # "nombre": "Roberto",
    # "apellido": "Aguirre"
# }

# user = {
#     "id" : 1,
#     "nombre": "Roberto",
#     "apellido": "Aguirre"
# }


# usuarios.append(id[1])
# print(usuarios)
# print(user.keys())

# id_usuario = id[1].get("id")
# print(usuarios[1].get("id"))

# contador_registro = 4
# usuarios_registro = 3
# print(contador_registro>usuarios_registro)
# if contador_registro<usuarios_registro:
#     input("Presionar cualquier boton para volver al menu...")

lista_usuario = [{ "id" : 1,"nombre": "Roberto","apellido":"Aguirre"},{ "id" : 2,"nombre": "Ivan","apellido":"Silerio"}]

####### !            Aceptado            ###################

for index in range(len(lista_usuario)):
    info_lista = lista_usuario[index]
    # print(info_lista)
    print("| ID",info_lista["id"],"|",info_lista["nombre"],info_lista["apellido"])


# for dic in use:
#     for val,cal in dic.items():
#         print(f'{val} is {cal}')


# for index in range(len(dataList)):
#     for key in dataList[index]:
#         print(dataList[index][key])