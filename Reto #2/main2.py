#Codigo creado por Roberto Ivan Aguirre Silerio para la semana de #RetoPython.Gracias.

print("$$$$$$$$$$ INGRESAR SOLO NUMEROS $$$$$$$$$$$$$")
usuarios_registro = int(input("Ingresa la cantidad de usuarios a dar de alta: "))
contador_registro = 1

if type(usuarios_registro) == int : 
    while contador_registro <= usuarios_registro:
        #Ingresa el valor del nombre y hace la verificacion
        nombres_usuario = str(input("Ingresa tu nombre(s): "))
        while len(nombres_usuario) < 5 or len(nombres_usuario) > 50:
            print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
            nombres_usuario = str(input("Ingresa tu nombre(s): "))
        #Ingresa el valor del nombre y verifica. 
        apellido_usuario = str(input("Ingresa tus apellidos: "))
        while len(apellido_usuario) < 5 or len(apellido_usuario) > 50:
            print("\nIngresa una cantidad minima de 5 caracteres y menor de 50.")
            apellido_usuario = str(input("Ingresa tus apellidos: "))

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
        print(type(nombres_usuario),type(apellido_usuario),type(telefono_usuario),type(email_usuario))
        print("\n Hola " + nombres_usuario +" "+ apellido_usuario + ", en breve recibiras un correo a " + email_usuario)
