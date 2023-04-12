"""Escriba un programa donde tendrá los siguientes requisitos:
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato)
- Un método cumpleaños donde cada vez que invoque aumentará en un año la
edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)"""

# Importamos una libreria para el tiempo

from datetime import datetime, date


# crear clase llamada Persona


class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        x = 1
        while x != 0:
            try:
                self.edad = int(input("Ingrese la edad: "))
                x -= 1
            except ValueError:
                print("Esa no es una edad valida")
        self._nacionalidad = "Peruana"

    # metodo cumpleaños

    def cumple(self):
        self.edad += 1


tiempo1 = datetime.now()
persona1 = Persona()

print("La primera persona llamada {}, es de nacionalidad {} y tiene {} años.".format(persona1.nombre, persona1._nacionalidad, persona1.edad))

persona1.cumple()
persona1.cumple()

print("Luego de 2 cumpleaños, {} tiene {} años.".format(persona1.nombre, persona1.edad))


def hora(a):
    print("{} se registró exactamente en: {}".format(a, tiempo1))


hora(persona1.nombre)