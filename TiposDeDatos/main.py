print("TIPOS DE VARIABLES")
print("Int:")
variable = 1
variable2 = 5
print(type(variable))
print("String:")
variable = "Hola Samantha"
print(type(variable))
print("Boolean:")
variable = True
print(type(variable))
print("CONCATENAR VARIABLES:")
cont = "Hola"
print("Este es el valor de la variable" + cont)
print("Aqui se junta las variables con una coma", cont, variable, variable2 + variable)
print("INGRESO DE DATOS POR INPUT")
entrada = int(input("Ingrese un numero de entrada: "))
valor2= int(input("Ingrese el segundo valor:"))
print("La suma de los dos numero es: ",entrada+valor2)
print("CALIFICA TU DIA:")
ValorDia=int(input("Califica tu día del 1 al 10:"))
print("Tu valor del dia fue:",ValorDia)
print("EJERCICIO DE LIBRO")
titulo = input("Proporciona el titulo del libro: ")
autor=input("Proporciona el nombre del autor: ")
print(titulo,"fue escrito por",autor)

