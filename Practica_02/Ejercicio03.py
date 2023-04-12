"""Escribir un programa para gestionar los errores en Python
Reglas:
- El programa deberá tener una función para ingresar dos datos los
cuáles serán ingresado por consola.
- Deberá tener una función en el caso haya una división entre cero y
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos.
- Todas las funciones creadas tendrás la facultad de volver a pedir el
número hasta que se ingrese correctamente."""


def operacion():
    prueba1 = 1
    prueba2 = 1
    while prueba1 != 0:
        try:
            v1 = int(input("Ingrese el primer valor para una división: "))
            v2 = int(input("Ingrese el segundo valor para una división: "))
            v3 = v1/v2
            prueba1 -= 1
            print("El resultado de dividir {} entre {} es {}.".format(v1, v2, v3))
        except ZeroDivisionError:
            print("¡No se puede dividir entre cero! Intentelo denuevo")
        except ValueError:
            print("¡No puedes dividir strings! Intentalo denuevo")
    while prueba2 != 0:
        try:
            a1 = int(input("Ingrese el primer valor para una suma: "))
            a2 = int(input("Ingrese el segundo valor para una suma: "))
            a3 = a1 + a2
            prueba2 -= 1
            print("El resultado de sumar {} más {} es {}.".format(a1, a2, a3))
        except ValueError:
            print("¡No se pueden sumar strings con enteros! Intentelo denuevo")


operacion()

