"""Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono y el email. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto"""

class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar(self,contacto,numero,mail):
        self.contactos[contacto] = "Telefono: " + numero + " Email: " + mail

    def mostrar(self):
        return print(self.contactos)

    def buscar(self,contacto1):
        return print(self.contactos[contacto1])

agenda1 = Agenda()
agenda1.agregar("Eduardo","999888333","pepe_juancho@gmail.com")
agenda1.mostrar()
agenda1.buscar("Eduardo")