# Variables y tipos de datos.

# nombre_de_la_variables = valor
# first_name = 'Roberto Ivan' # String "" o '' 
# last_name = "Aguirre Silerio"

# full_name = first_name + " "+ last_name

# age = 38
# score = 9.3
# active = True

# print(age)
# print(score)
# print(active)

#Son variables 

# result = type(full_name)

# print(result)

name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
score = float(input("Ingres tu calificacion: "))
active = input("Sigue activo? : ") == "Si"

print(name,age,score,active)
print(type(name),type(age),type(score),type(active))

#snake_case
#funciones input - int - float - str 