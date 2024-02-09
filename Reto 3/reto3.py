#Codigo creado por Roberto Ivan Aguirre Silerio para la semana de #RetoPython.Gracias.

print("\n$$$$$$$$$$ INGRESAR SOLO NUMEROS $$$$$$$$$$$$$\n")
usuarios_registro = int(input("Ingresa la cantidad de usuarios a dar de alta: "))
contador_registro = 1
id_autoincremnt = 1
listado_ids = []
listado_usuarios = []

if type(usuarios_registro) == int : 
    while contador_registro <= usuarios_registro:
        #Ingresa el valor del nombre y hace la verificacion
        nombres_usuarios = str(input("\nIngresa tu nombre(s): "))
        while len(nombres_usuarios) < 5 or len(nombres_usuarios) > 50:
            print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
            nombres_usuarios = str(input("Ingresa tu nombre(s): "))
        #Ingresa el valor del nombre y verifica. 
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
       
        listado_ids.append(id_autoincremnt)
        listado_usuarios.append(nombres_usuarios+" "+apellido_usuarios)

        id_autoincremnt +=1
       
    for index,listado_id in enumerate(listado_ids):
        print("|ID",listado_ids[index],"|Nombre:",listado_usuarios[index])