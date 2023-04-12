"""manejo de impresión de valores de una cadena de caracteres
tercer modo de imprimir valores"""

nombre=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")

print(f"Bienvenido/a {nombre}, usted tiene {edad} años.")

#cuarto modo de imprimir valores

print("Bienvenido/a {nombre_usuario}, usted tiene {edad_usuario} años.".format(nombre_usuario=nombre, edad_usuario=edad))