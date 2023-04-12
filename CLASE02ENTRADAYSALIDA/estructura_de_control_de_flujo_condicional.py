"""estructura de control de flujo condicionales
if"""
#edad=int(input("Ingrese su edad: "))
edad=10
if 110>=edad>=18:
    print("Usted es mayor de edad.")
elif 0<=edad<18:
    print("Usted es menor de edad.")
else:
    print("No creo que usted esté siendo honesto con su edad.")

a=int(input("ingresa el valor 1: "))
b=int(input("ingresa el valor 2: "))

if a>b:
    print("el valor 1 es mayor al valor 2")
elif b>a:
    print("el valor 2 es mayor al valor 1")
else:
    print("Ambos valores son iguales")