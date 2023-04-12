"""Manejo de errores"""

#
# def operaciones(a, b):
#     try:
#         c = a/b
#         return c
#     except TypeError:
#         return "¡No puedes operar números con cadenas!"
#     except ZeroDivisionError:
#         return "¡No se puede dividir entre cero!"
#     except:
#         return "¡Qué hiciste, mi querido!"
#
# print(operaciones(32,"s"))


def operaciones(a, b):
    try:
        resultado = a+b
        #resultado = a/b
        return print(resultado)
    except (TypeError, ZeroDivisionError):
        return print("Excepción ZeroDivisionError/TypeError.")


operaciones(4, "hola")
operaciones(10,24)

