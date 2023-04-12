from funciones import suma,multiplicar

var1 = int(input("Ingrese el primer valor: "))
var2 = int(input("Ingrese el segundo valor: "))

sum = suma(var1, var2)
mult = multiplicar(var1, var2)

print("La suma y producto de los valores son: {} y {}".format(sum,mult))

