"""POO en Python"""
"""Polimorfismo"""


class Perro:
    def sonido(self):
        print("WOOF WOOF")


class Gato:
    def sonido(self):
        print("MEOW MEOW NI")


class Vaca:
    def sonido(self):
        print("MOOO MOOO M")


perro, gato, vaca = Perro(), Gato(), Vaca()
lista_animales=[perro,gato,vaca]


def canto(animales):
    for animal in animales:
        animal.sonido()

canto(lista_animales)