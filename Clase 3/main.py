# Las listas son una estructura de datos
#separados por comas

# my_list = [1,3.14, "String", True, [2,3.111,"Example",False]]
# print(my_list)
# print(type(my_list))
#Lista homogeneas con un solo tipo de elemento


#Indices     0         1        2      3           4           5     6
#Inversos     -7      -6       -5     -4          -3          -2    -1
courses = ["Python","Django","Flask","Ruby","Ruby on Rails","Rust","C#"] # 5-1

# Indice que empieza y hasta cual
# new_list = courses[2:6]

#Indice que empieza y todos los demas.
# new_list = courses[3:]
# #Desde el inicio hasta n elementos.
# new_list = courses[:5]

#Saltos de elementos #Como si fueran los par
# new_list = courses[::2]

#Genera una sublista a la inversa
new_list = courses[::-1]


print(new_list)

#Pedir un numero y devuelve el elemento en esa posicion
# last_index = len(courses)-1
# index = int(input("Ingresa el numero a buscar: "))

# if index<=last_index:
#     print(courses[index])
# else: 
    # print("El numero no existe")


# print(courses[4])
# print(last_index)