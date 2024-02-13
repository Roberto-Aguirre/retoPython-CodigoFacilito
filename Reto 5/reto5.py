#Codigo creado por Roberto Ivan Aguirre Silerio para la semana de #RetoPython.Gracias. 
import os

lista_usuario = []

##? Metodo para limpiar la consola
os.system('cls')

print("\n$$$$$$$$$$ INGRESAR SOLO NUMEROS $$$$$$$$$$$$$\n")

print("Bienvenido al sistema de gestion de usuarios")
print("Se encuentran las siguientes opciones en el sistemas:")
print("1.Añadir usuarios")
print("5.Salir")
print("\nNota:Deberas haber dado de alta al menos un usuario para editar, visualizar y modificarlos")

# opcion_usuario = int(input(">> "))
# def menu_inicial():
#     os.system('cls')

#     print("\n$$$$$$$$$$ INGRESAR SOLO NUMEROS $$$$$$$$$$$$$\n")

#     print("Bienvenido al sistema de gestion de usuarios")
#     print("Se encuentran las siguientes opciones en el sistemas:")
#     print("1.Añadir usuarios")
#     print("5.Salir")
#     print("\nNota:Deberas haber dado de alta al menos un usuario para editar, visualizar y modificarlos")

#     opcion_usuario = int(input(">> "))

# usuarios_registro,contador_registro = 0,0

# while opcion_usuario != 5:
#     ## ! Añadir usuario
#     if opcion_usuario == 1:
#             os.system('cls')
#             if usuarios_registro<contador_registro:
#                 input("Presionar cualquier boton para volver al menu...")
#             else:
#                 os.system('cls')
#                 print("Bienvenido al sistema de gestion de usuarios")
#                 print("Se encuentran las siguientes opciones en el sistemas:")
#                 print("1.Añadir usuarios")
#                 print("2.Usuarios dados de alta.")
#                 print("3.Consultar usuario por ID")
#                 print("4.Editar usuario por ID")
#                 print("5.Salir")
#                 opcion_usuario = int(input(">> "))
                        
#     ## ! Listar usuarios
#     elif opcion_usuario ==2:
#         os.system('cls')
#         print("Lista de usuarios dados de alta")
#         print("| ID   | Nombre Completo")
#         for index in range(len(lista_usuario)):
#             info_lista = lista_usuario[index]
#             print("| ID",info_lista["id"],"|",info_lista["nombre"],info_lista["apellido"])
#         input("Presionar cualquier boton para volver al menu...")
#         os.system('cls')
#         print("\nBienvenido al sistema de gestion de usuarios")
#         print("Se encuentran las siguientes opciones en el sistemas:")
#         print("1.Añadir usuarios")
#         print("2.Usuarios dados de alta.")
#         print("3.Consultar usuario por ID")
#         print("4.Editar usuario por ID")
#         print("5.Salir")
#         opcion_usuario = int(input(">> "))

#     ## ! Ver informacion de un ID
#     elif opcion_usuario ==3:
#         os.system('cls')
#         consulta_id = int(input("Ingresa el Id a consultar: "))
        
#         if consulta_id<=len(lista_usuario):
#             os.system('cls')

#             user_consulta = lista_usuario[consulta_id-1]
#             print("ID: ",int(user_consulta["id"]))
#             print("Nombre(s): "+user_consulta["nombre"])
#             print("Apellido(s): "+user_consulta["apellido"])
#             print("Telefono: ",int(user_consulta["tel"]))
#             print("Email: "+user_consulta["email"])
#             input("\nPresionar cualquier boton para volver al menu...")
            
#         else: 
#             print("ID no encontrada o usuario no existe")
#             input("\nPresionar cualquier boton para volver al menu...")
             

#     elif opcion_usuario ==4:
#         os.system('cls')

#         editar_id=int(input("Ingresa el id a editar: "))
#         if editar_id<=len(lista_usuario):
#             user_editar = lista_usuario[editar_id-1]
#             print(user_editar)
#             #Ingresa el valor del nombre y hace la verificacion
#             nombres_usuarios = str(input("\nIngresa tu nombre(s): "))
#             while len(nombres_usuarios) < 5 or len(nombres_usuarios) > 50:
#                 print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
#                 nombres_usuarios = str(input("Ingresa tu nombre(s): "))
            
#             #Ingresa el valor del apellido y verifica. 
#             apellido_usuarios = str(input("Ingresa tus apellidos: "))
#             while len(apellido_usuarios) < 5 or len(apellido_usuarios) > 50:
#                 print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
#                 apellido_usuarios = str(input("Ingresa tus apellidos: "))

#             #Ingresa el valor del telefono y verifica.
#             telefono_usuario = str(input("Ingresa tu numero celular: "))
#             while len(telefono_usuario) < 10 or len(telefono_usuario) > 10 :
#                 print("\nSe necesitan al menos 10 digitos.")
#                 telefono_usuario = str(input("Ingresa tu numero celular: "))

#             telefono_usuario = int(telefono_usuario)
            
#             #Ingresa el valor de email
#             email_usuario = str(input("Ingresa tu correo electronico: "))
#             while len(email_usuario) < 5 or len(email_usuario) > 50:
#                 print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
#                 email_usuario = str(input("Ingresa tu correo electronico: "))

#             lista_usuario[editar_id-1] = {"id":ultimo_index,"nombre":nombres_usuarios,"apellido":apellido_usuarios,"tel":telefono_usuario,"email":email_usuario}

#         else:    
#             print("ID no encontrada o usuario no existe")
#             input("\nPresionar cualquier boton para volver al menu...")
        
#         os.system('cls')
#         print("Bienvenido al sistema de gestion de usuarios")
#         print("Se encuentran las siguientes opciones en el sistemas:")
#         print("1.Añadir usuarios")
#         print("2.Usuarios dados de alta.")
#         print("3.Consultar usuario por ID")
#         print("4.Editar usuario por ID")
#         print("5.Salir")
#         opcion_usuario = int(input(">> "))    
#     else:
#         os.system('cls')
#         print("Bienvenido al sistema de gestion de usuarios")
#         print("Se encuentran las siguientes opciones en el sistemas:")
#         print("1.Añadir usuarios")
#         print("2.Usuarios dados de alta.")
#         print("3.Consultar usuario por ID")
#         print("4.Editar usuario por ID")
#         print("5.Salir")
#         opcion_usuario = int(input(">> "))    

def menu():    
    os.system('cls')
    print("Bienvenido al sistema de gestion de usuarios")
    print("Se encuentran las siguientes opciones en el sistemas:")
    print("1.Añadir usuarios")
    print("2.Usuarios dados de alta.")
    print("3.Consultar usuario por ID")
    print("4.Editar usuario por ID")
    print("5.Salir")
    
    return int(input(">> ")) 

def add_user_form():
    usuarios_registro = int(input("Ingresa la cantidad de usuarios a dar de alta: "))
    if type(usuarios_registro) == int : 
        contador_registro = 1
        while contador_registro <= usuarios_registro:
            #Ingresa el valor del nombre y hace la verificacion
            nombres_usuarios = str(input("\nIngresa tu nombre(s): "))
            while len(nombres_usuarios) < 5 or len(nombres_usuarios) > 50:
                print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
                nombres_usuarios = str(input("Ingresa tu nombre(s): "))
            
            #Ingresa el valor del apellido y verifica. 
            apellido_usuarios = str(input("Ingresa tus apellidos: "))
            while len(apellido_usuarios) < 5 or len(apellido_usuarios) > 50:
                print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
                apellido_usuarios = str(input("Ingresa tus apellidos: "))

            #Ingresa el valor del telefono y verifica.
            telefono_usuario = str(input("Ingresa tu numero celular: "))
            while len(telefono_usuario) < 10 or len(telefono_usuario) > 10 :
                print("\nSe necesitan al menos 10 digitos.")
                telefono_usuario = str(input("Ingresa tu numero celular: "))

            telefono_usuario = int(telefono_usuario)
            
            #Ingresa el valor de email
            email_usuario = str(input("Ingresa tu correo electronico: "))
            while len(email_usuario) < 5 or len(email_usuario) > 50:
                print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
                email_usuario = str(input("Ingresa tu correo electronico: "))
            
            contador_registro+=1

    return nombres_usuarios,apellido_usuarios,telefono_usuario,email_usuario

# def success_fail(estado):
#     if estado>=0:
#         print("Se dio de alta al usuario")
#         input("\nPresionar cualquier boton para volver al menu...")
#     else:
#         print("ID no encontrada o usuario no existe")
#         input("\nPresionar cualquier boton para volver al menu...")



def new_user(nombres_usuarios="",apellido_usuarios="",telefono_usuario="",email_usuario=""):
    ultimo_index = len(lista_usuario)+1
    lista_usuario.append({"id":ultimo_index,"nombre":nombres_usuarios,"apellido":apellido_usuarios,"tel":telefono_usuario,"email":email_usuario})
    return lista_usuario
    


match menu():
    case 1: 
        
        info = add_user_form()
        new_user(info)
        input(lista_usuario)