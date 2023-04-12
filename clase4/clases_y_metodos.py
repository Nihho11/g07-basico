"""Programacion orientada a objetos con Python
clase y métodos"""


class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: valores que van a tener por defecto mi clase cuando se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
    """Métodos: son las funciones de la clase"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion


    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad<0:
            velocidad = 0
        self.velocidad = velocidad

carro1 = Carro("Azul",90)

print("La velocidad inicial de mi carro 1 es: {}".format(carro1.velocidad))

carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()

carro1.frena()
carro1.frena()

print("La velocidad después de una aceleración de mi carro 1 es: {}".format(carro1.velocidad))