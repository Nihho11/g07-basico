"""Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo-encapsulamiento) (sueldo superior a
4000)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto."""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, sueldo):
        self.sueldo = sueldo

    def impuesto(self):
        return print("Debe pagar impuesto de: " + str(0.1*self.sueldo) if self.sueldo >= 4000 else "No debe pagar impuesto")


empleado1 = Empleado(4001)

empleado1.nombre = "Eduardo"
empleado1.edad =  22
empleado1.impuesto()
