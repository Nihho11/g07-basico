"""Herencia en clases"""
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

#es una clase hija:

class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando = False):
        super().__init__(color, aceleracion)
        self.estado_volando = estado_volando

    def vuela(self):
        self.estado_volando = True

    def aterriza(self):
        self.estado_volando = False

carro1 = Carro("Rojo", 70)

carro_volador = CarroVolador("Blanco",50)

print("Color de mi carro volador: {}".format(carro_volador.color))
print("El estado inicial de mi carro volador es: {}".format("No volando" if not carro_volador.estado_volando else "volando"))

carro_volador.acelerar()
carro_volador.vuela()

print("Velocidad del carro volador: ", carro_volador.velocidad)
print("estado de vuelvo: ", "No volando" if not carro_volador.estado_volando else "Volando")

print(carro_volador.ruedas)


#La herencia es solo sobre la clase HIJA, no puede usar por ejemplo, el estado de vuelvo en el carro1 pues no tiene el atributo de vuelo