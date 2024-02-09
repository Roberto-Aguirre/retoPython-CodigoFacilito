# Las listas son una estructura de datos
#separados por comas
#Se vera lo siguiente
#### append, insert, remove, count, index
##Append - Agregar al final
##insert - ingresas en un indice exacto y lo demas se desplaza (index,elemento)
##count - cuenta cuantos elementos tiene el array
##index - conocer en que posicion se encuentra un valor
##extend - agregar una lista a otra.

# my_list = [1,3.14, "String", True, [2,3.111,"Example",False]]
# print(my_list)
# print(type(my_list))
#Lista homogeneas con un solo tipo de elemento


############# Creando arrays

#Indices     0         1        2      3           4           5     6
#Inversos     -7      -6       -5     -4          -3          -2    -1
courses = ["Python","Django","Flask","Ruby","Ruby on Rails","Rust","C#"] # 5-1

########### Seleccionar los elementos que queremos

# Indice que empieza y hasta cual
# new_list = courses[2:6]

#Indice que empieza y todos los demas.
# new_list = courses[3:]
# #Desde el inicio hasta n elementos.
# new_list = courses[:5]

#Saltos de elementos #Como si fueran los par
# new_list = courses[::2]

#Genera una sublista a la inversa
# new_list = courses[::-1]
# print(new_list)

#Pedir un numero y devuelve el elemento en esa posicion
# last_index = len(courses)-1
# index = int(input("Ingresa el numero a buscar: "))

# if index<=last_index:
#     print(courses[index])
# else: 
    # print("El numero no existe")

######################### Sustituir valor

# courses[1] = "Django 1.14"
# print(courses[1])

######################### append - poner elementos al final

courses.append("Javascript")
courses.append("TypeScript")
courses.append("Swift")

######################### insert - Desplazar al indice que usamos a la derecha
courses.insert(1,"SQLServer")

new_courses = ["Java8", "Docker", "Unix"]

#Los ingresa al final


######################## extend - juntar varias listas

courses.extend(new_courses)

####################### remove - Eliminar elemento de una lista  - lista.remove("texto")
# courses.remove("Python")
# courses.remove("C#")
# courses.remove("Flask")

# print(courses.count("Python"))
# # print(courses.count("Java8"))
# #Saber si esta o no
# ##Recomendaciones de usar in
# print("Ruby" in courses)

#####################           Index
# print(courses.index("Python"))
# print(courses[0])
print(courses)

# value= "Laravel"
value= "Python"

if value in courses:
    print("El indice es: " + str(courses.index(value)))
else:
    print("Lo sentimos, el valor no existe dentro de la listas")


###################                 Clear
# courses.clear()
# print(courses)
# print(len(courses))    
    
###################                 foreach
    
# for courses in courses:
#     print(courses)
# for course in new_courses:
#     courses.append(course)

# print(courses)

###################                  enumerate
# for index,course in enumerate(courses):
#     print("El valor para el indice ",index," es ",course)

# for index,character in enumerate("Hola mundo"):
#     print("EL valor para el indice ", index, " es :",character)
##Revertir el string    
# print("Hola mundo"[::-1])
