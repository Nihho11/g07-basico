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

"""Instansiar nuestra clase"""

carro1 = Carro("Gris",10)

print("El color del primer carro es: {}".format(carro1.color))
print("La aceleración del primer carro es: {}".format(carro1.aceleracion))
print("Las ruedas de mi primer carro son: {}".format(carro1.ruedas))

carro2 = Carro("Rojo",70)

print("El color del segundo carro es: {}".format(carro2.color))
print("La aceleración del segundo carro es: {}".format(carro2.aceleracion))
print("Las ruedas de mi segundo carro son: {}".format(carro2.ruedas))

"""En los ejemplos vistos carro1 y carro2 son objetos cuya clase es Carro
ambos objetos tienen la propiedad de acelerar y frenar"""

"""Para crear un objeto de una clase especifica, osea, instanciar una clase, se escribre:
obj = MiClase() """

"""Métodos son funciones definidas dentro de la clase"""

carro3 = Carro("Blanco",40)

print("El color del tercer carro es: {}".format(carro3.color))

carro4 = Carro("Rojo", 80)
carro4.marchas = 30000

print("El número de marchas de mi cuarto carro es: {}".format(carro4.marchas))

#IMPORTANTE:
#no es posible llamar un atributo de datos que se le ha asignado a otra instancia de la clase
#este objeto no tiene el atributo marchas, nos dará un error
#print("El número de marchas de mi primer carro es: {}".format(carro1.marchas))

