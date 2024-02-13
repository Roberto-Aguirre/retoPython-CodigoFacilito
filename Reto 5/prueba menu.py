import os

def imprimir():
    print("hola mundo")

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

print(menu())

match menu():
    case 1: new_user()