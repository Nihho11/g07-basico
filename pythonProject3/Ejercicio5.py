"""Programa para ver si es par o impar"""

#creamos un condicional si el modulo entre 2 es 0 es par sino es impar
#utilizamos una simplifación pues sabemos que el número 0 se puede interpretar como False y por lo tanto el 1 como
#True de modo que el condicional se puede escribir como

#pedimos al usuario ingresar el valor del sueldo
Sueldo=input("ingrese el sueldo (número entero) para saber si es par o impar: ")
#convertimos en entero
Sueldoint=int(Sueldo)
#condicional

if Sueldoint%2:
    print("Es impar")
else:
    print("Es par")