"""
8. Solicitar a un usuario ingresas su nombre y apellidos, para lo cual se solicitar mostrar en pantalla solamente sus dos apellidos

"""

nombre = input("Ingrese su nombre completo: ")


def apellidos(x):
    return x.split()[-2] + " " + x.split()[-1]


print("Sus apellidos son: {}".format(apellidos(nombre)))