"""Usando tipos de datos y sus conversiones realizar:"""

#pedir por consola nombre y edad

nombre=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")

#edad tiene que ser entero

edadint=int(edad)

#identificar tipos ingresados

print("Los tipos de datos de nombre y edad respectivamente son {} y {} pero transformamos el dato edad a {}".format(type(nombre),type(edad),type(edadint)))

#pedir nombre y edad y sumar

nombre1=input("La primera persona se llama: ")
nombre2=input("La segunda persona se llama: ")
edad1=input("La primera edad es: ")
edad2=input("La segundad edad es: ")

edad1int=int(edad1)
edad2int=int(edad2)

print("La suma de las edades de {} y {} resulta {}".format(nombre1,nombre2,edad1int+edad2int))