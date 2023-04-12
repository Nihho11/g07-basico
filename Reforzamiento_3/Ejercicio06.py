"""Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, imprimirlos y un método para mostrar un mensaje con el
resultado de la nota y si ha aprobado (mayor o igual a 11) o no el alumno.
Instanciar la clase por lo menos 3 veces."""

class Alumno():
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
        self._nota_final = int(input("Ingrese su nota final: "))

    def mostrar_datos(self):
        return print("Nombre, edad y nota de el/la alumno/a: {}, {} y {}".format(self.nombre, self.edad, self._nota_final))

    def estado(self):
        return print("Está aprobado con: {}".format(self._nota_final)) if self._nota_final >= 11 else print("Desaprobó con: {}".format(self._nota_final))


alumno1 = Alumno()
alumno1.mostrar_datos()
alumno1.estado()

alumno2 = Alumno()
alumno2.mostrar_datos()
alumno2.estado()

alumno3 = Alumno()
alumno3.mostrar_datos()
alumno3.estado()


