"""Programación funcional en Python"""

val1 = 10
val2 = 34


#Input: dos variables que pasarán por parámetros de la función
#x,y: parámetros de la función "suma"


def suma(x,y):
    return x+y


resultado = suma(val1,val2)

print("El resultado de {} más {} es: {}.".format(val1,val2,resultado))

#funcion con parametros


def mult(a,b=10):
    return a*b

print(mult(3))
print(mult(7,11))
print(mult(1))

