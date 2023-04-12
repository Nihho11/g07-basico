# while True:
#     try:
#         x=int(input("Por favor ingresar un número: "))
#         break
#     except ValueError:
#         print("Oops, ese no es un número.")
#

"""Manejo de errores"""
"""Error de sintaxis"""

# contador = 0
#
# while contador<10:
#     contador += 1
#     print(contador)


# division entre 0
# while True:
#     try:
#         a = 100/0
#         break
#     except ZeroDivisionError:
#         print("Que haces oe")

"""Tipo de error: suma de dos tipos diferentes de datos"""
# TypeError
# suma = 100 + "Pythonator"

"""Más errores:
OverflowError
IndexError
KeyError
FileNotFoundError
ImportError
"""

"""Estructura y uso

    try:
        bloque de código 1
    except "excepción_1":
        bloque de código 2
    else:
        bloque de código 3
"""


def division(a,b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("¡No se puede divir entre cero!")
    else:
        print(resultado)


division(40, 0)
division(1000, 50)