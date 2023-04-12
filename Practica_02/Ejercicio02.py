"""Usando el concepto de herencia y encapsulación (para saldo) para crear el
siguiente programa:
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia(self, persona2, monto)
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método trasnferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas."""

# clase persona del ejercicio anterior


class Persona:
    def __init__(self, nombre, edad):
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


class Empleado(Persona):
    def __init__(self,nombre, edad, saldo):
        super().__init__(nombre, edad)
        self.saldo = saldo

    def transferencia(self, persona2, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            persona2.saldo += monto
        else:
            print("Saldo insuficiente")


persona01 = Empleado("Pepe", 19, 1000)
persona02 = Empleado("Hugo", 22, 1500)

print("{} tiene {} antes de la transferencia.".format(persona01.nombre, persona01.saldo))
print("{} tiene {} antes de la transferencia.".format(persona02.nombre, persona02.saldo))

a = 1

while a != 0:
    try:
        monto1 = int(input("¿Cuánto dinero quiere transferir? "))
        a -= 1
    except ValueError:
        print("¡Ingrese un monto valido!")

persona01.transferencia(persona02,monto1)

print("{} tiene {} despues de la transferencia.".format(persona01.nombre, persona01.saldo))
print("{} tiene {} despues de la transferencia.".format(persona02.nombre, persona02.saldo))




