nombre = input("ingresa tu nombre: ")
apellido = input("ingresa tu apellido paterno: ")
nombre_completo = "{} {}".format(nombre,apellido)
size = len(nombre_completo)
print("NOMBRE COMPLETO: {}".format(nombre_completo.upper()))

if len(nombre) > len(apellido):
    print("El nombre es más largo que el apellido")
elif len(apellido) > len(nombre):
    print("el apellido es más largo que el nombre")
else:
    print("son igual de largos")