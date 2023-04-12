"""Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)"""

def nombre(a, b):
    nombre_completo = a + " " + b
    return print("Su nombre completo es {}".format(nombre_completo))

def seguro(a):
    return print("Usted tiene el seguro " + a)

def mayor_edad(a):
    if a>=18:
        return print("Usted es mayor de edad")
    else:
        return print("Usted es menor de edad")