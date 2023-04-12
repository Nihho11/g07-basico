"""Función de resta en python"""


def resta(a, b):
    return a - b


a1 = int(input("El primer número para la resta es: "))
a2 = int(input("El segundo número para la resta es: "))

resultado = resta(a1, a2)

print("El resultado de restar {} a {} es: {}".format(a2, a1, resultado))
