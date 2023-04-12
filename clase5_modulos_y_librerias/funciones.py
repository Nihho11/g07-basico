def suma(a, b):
    return a+b


def resta(a,b):
    return a-b


def multiplicar(a, b):
    return a*b


def dividir(a, b):
    try:
        c = a/b
        return c
    except ZeroDivisionError:
        return ("¡No puedes dividir entre cero!")