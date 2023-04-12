"""usando las propiedades de cadenas o strings"""

cadena="Lenguaje de programación"
print("El tamaño de mi cadena es: {}".format(len(cadena)))

print("La primera palabra de mi cadena es: {}".format(cadena[0:8]))

print("El último valor de mi cadena es: {}".format(cadena[-1]))

#concatenación

nombre="Caro"
apellido="Vinsmoke"
nombre_completo= nombre + " " + apellido
print(nombre_completo)

"""Usando el formato de format"""

nombre_completo_2 = "El nombre completo del usuario es: {} {}".format(nombre, apellido)

print(nombre_completo_2)

str1 = "{} {}".format(nombre,apellido)

print(str1)

#multiplicar strings

str2="hola si "

print(str2*4)

"""Métodos de Strings"""

str10="Hola mundo, este programa fue hecho en Python"

print(str10.title())
print(str10.upper())
print(str10.lower())