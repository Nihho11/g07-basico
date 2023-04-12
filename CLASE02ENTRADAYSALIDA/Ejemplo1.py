"""Ejercicio de clase
alumno: Eduardo Haro Villanueva"""

"""
Requisitos:
-Ingresar tu nombre y apellido por consola (cada valor en una variable diferente)
-Concatenar ambos valores en una variable
-Obtener el tamaño de tu nombre completo
-Imprimir el resultado final todo por mayúscula"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su appellido: ")

nombre_completo = "{} {}".format(nombre, apellido)

size = len(nombre_completo)

print("EL NOMBRE COMPLETO EN MAYUSCULA ES {} Y TIENE EL TAMAÑO DE {}".format(nombre_completo.upper(),size))