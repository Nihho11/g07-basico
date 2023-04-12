"""Crear una clase llamada círculo que contenga radio (en el constructor),
y que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios."""


class Circulo:
    def __init__(self):
        self.radio = 0
        try:
            self.radio = int(input("Ingresa un radio para el círculo: "))
        except ValueError:
            print("Ese no es un número.")

    def area(self):
        return 3.14*self.radio**2

    def perimetro(self):
        return 2*3.14*self.radio


circulo1 = Circulo()
circulo1.radio
if circulo1.area() != 0:
    print("El area y perimetro del circulo son: {} y {}.".format(circulo1.area(), circulo1.perimetro()))
