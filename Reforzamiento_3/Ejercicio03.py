"""Crear una clase que contengo dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados. Comprobar ambos métodos instanciado la
clase respectivamente"""

class Ejercicio3:
    def nombres(self):
        self.name = input("Ingrese su nombre completo: ")

    def edad(self):
        self.age = input("Ingrese su edad: ")

    def mostrar(self):
        return print("Buenas, {}, usted tiene {} años.".format(self.name, self.age))


ejemplo1 = Ejercicio3()
ejemplo1.nombres()
ejemplo1.edad()
ejemplo1.mostrar()