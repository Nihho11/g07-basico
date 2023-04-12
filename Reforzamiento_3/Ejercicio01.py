"""Escribir una clase en python que contenga un método que convierta un
número entero en su cubo."""


class Cubo:
    def __init__(self,num):
        self.cubo = num**3


numero = int(input("Introduce un número entero: "))
num_cub = Cubo(numero)

print("El número al cubo es: ", num_cub.cubo)
