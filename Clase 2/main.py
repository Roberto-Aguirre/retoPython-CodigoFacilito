#Estructras de control
#if,match(switch), foreach, while

# #bool
# #Operadores relacioanles ( ==, !=, > , < , >=, <= )
# #Operadores logicos (and, or, not)

# num1 = 10
# num2 = 20

# # # result = False or False or False or True
# # result = True and (True and (not (False and (True or False))))
# # print(result)

# if <condition(True/False)> : 
# pass ← Pasa a a siguiente linea 

# age = int(input("Ingresa tu edad: ")) #String to int

# if age < 110: 
#     if age >= 18:
#         print("Tienes la edad para votar")
#     else: 
#         print("Lo siento, no puedes votar")

# else: 
#     print("La edad no es valida, intenta de nuevo")

# color = "red"

# if color == "green":
#     print("Puede continuar")
# else: 
#     if color == "yellow": 
#         print("Alto parcial")
#     else:
#         if color == "red":
#             print("Alto total")

#### Refactor de codigo de arriba

# # if color == "green": 
# #     print("Puede continuar")
# # elif color == "yellow":
# #     print("Alto parcial")
# # elif color=="red": 
# #     print("Alto total")
# # else: print("El color no es valido.")

#Metodo match ( switch )

# color = "green"

# match color:
#     case "red":
#         print("Alto total")
#     case "yellow":
#         print("Alto parcial")
#     case "green":
#         print("Puede continuar")
#     case _:
#         print("Lo sentimos el color no es valido")

#foreach -> Cuando sepamos cuantas iteraciones se necesitan.

#while -> Cuando NO sepamos cuantas iteraciones se necesita(condicion)

# title = "Estructura de control"

# for caracter in title:
#     print(caracter)

# for number in range(1,101):
#     if number % 2 == 0: ## Numero par
#         print(number)

# while
# number = 0
# while number < 10:
#     print(number+1)
#     number+=1

# random = 5
# number = 0
# max_atteds = 5 
attends = 1
random,number,max_attends = 5,0,5

while number !=random and attends <= max_attends:
    number = int(input("Ingresa un numero: "))
    attends +=1
else: 
    if number == random:
        print("Felicidades encontraste el numero")   
    else:
        print("Lo siento no encontraste el numero secreto")