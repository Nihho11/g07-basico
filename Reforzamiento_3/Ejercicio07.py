"""Crear una clase Persona con los siguientes requerimientos. La clase
tendrá como atributos el nombre y la edad de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor) y un método para mostrar los datos e indicar si la
persona es mayor de edad o no.
Instanciar por lo menos la clase con 2 diferentes personas."""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        return print("La persona llamada " + self.nombre + ", de edad " + str(self.edad) + ", es " + ("mayor" if self.edad >= 18 else "menor") + " de edad.")


nombre1 = input("Ingrese un nombre: ")
edad = int(input("Ingrese una edad: "))
persona1 = Persona(nombre1, edad)

persona1.mostrar()