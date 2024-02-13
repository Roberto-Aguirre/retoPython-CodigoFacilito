#Funciones

# def nombre_funcion():
    #realizar la funcion

# def print_number():
#     for number in range(1,11):
#         print(number)

# print_number()S

## Si la funcion realiza una o más tareas debemos extraerlas y realizar otras funciones
##Los datos de entrada son argumentos = Argumentos -> Parametros



def suma(num1,num2):
    # result = num1+num     # tenemos variable facil
    return num1+num2,10
    #Retorna una tupla

suma(20,20)

# podemos extraer los valores
    #El Siguiente elemento se omitira
result,*_ = suma(10,20)

print(result)
## en el return hara un break para el codigo de abajo

##  Retornar varios valores


## Aplicacion que saque un promedio

scores = []

def set_score():
    for option in range(0,5):
        score = int(input("Ingresa una calificacion: "))
        scores.append(score)
    return scores
def average(scores):
    return sum(scores)/len(scores)
     

def show_mesagge(average):
    match average:
        case 10:
            print("Muchas felicidades aprobaste la materia...")
        case 9 | 8: 
            print("Aprobaste la materia.")
        case 7:
            print("Aprobaste a materia, pero necesitas practicar más")
        case _:
            print("Lo sentimos, no aprobaste la materia")

scores = set_score()
average = average(scores)
show_mesagge(average)
