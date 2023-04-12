"""Estructuras de control fijo
es una regla de buenas prácticas:
el código debe estar lo más compacto posible
"""

"""Asignación multiple
referente a dos o más variables"""

var1=input("Ingrese su nombre de usuario: ")
var2=input("Ingrese su nombre: ")
var3=input("Ingrese su edad: ")

#usuario=var1
#nombre=var2
#edad=var3

usuario, nombre, edad = var1, var2, var3

print("Su nombre de usuario es {}, su nombre es {} y su edad es {}.".format(usuario, nombre, edad))

"""Asignación multiple
en tupla"""

miTupla1=("Python","Backend","13 años")

nombreTecnologia, tipoTecnologia, antiguedad= miTupla1

print("El nombre, tipo y antiguedad de mi tecnología son respectivamente: {}, {} y {}.".format(nombreTecnologia,tipoTecnologia,antiguedad))

"""Asignación multiple
en listas"""

miLista1=["Python", "Backend", "13 años"]

nombreTec, tipoTec, anti= miLista1

print(nombreTec)
print(tipoTec)
print(anti)

