"""
    Crear 3 variables nombre, edad, distrito
    Requisitos:
    -Nombre= str, edad= int, Distrito= string
    -Concatenar estos 3 datos e indicar una oración como la siguiente:
    Jose tiene x años y es de 'Distrito'
    -Indicar el módulo de su edad al usarlo con el número 5
"""
# para la oración
nombre1 = "Bob Marley"
edad1 = 23
distrito1 = "Magdalena del Mar"

print("{} tiene {} años y es de {}".format(nombre1, edad1, distrito1))

# para el módulo

modu = edad1 % 5

print("el módulo de su edad al usarlo con 5 es {}".format(modu))
