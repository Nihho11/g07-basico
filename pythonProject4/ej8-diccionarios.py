"""diccionarios en python"""
"""Los nombres de los keys van a ir escritos en minúsculas (por convención)!!!"""

diccionario={"nombre": "Python","tipo":"Backend"}

print("Nuestro primer diccionario tiene el siguiente contenido: {}".format(diccionario))

"""Agregar elementos en un nuevo key a mi diccionario"""

diccionario["antiguedad"]="14 años"
diccionario["sistema operativo"]= "MacOS, Windows, Linux"

print("Mi diccionario actualizado es: {}".format(diccionario))

print("---------------------------------")
diccionario2={"nombre":"Alfredo","edad":28,"ciudad":"Lima"}

print("Mi diccionario actual es: {}".format(diccionario2))

"""para eliminar un key sin saber su valor 
usamos del"""

del diccionario2["edad"]

print("El diccionario actualizado es: {}".format(diccionario2))


