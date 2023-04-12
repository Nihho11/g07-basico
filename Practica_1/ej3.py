"""Concepto de diccionarios"""
#crear diccionario con keys nombre, apellidos, edad, dni

dic1={}

#pedir por consola los valores para estos keys

dic1["nombre"]=input("Ingrese el nombre que irá en el diccionario: ")
dic1["apellidos"]=input("Ingrese los apellidos: ")
dic1["edad"]=int(input("Ingrese la edad: "))
dic1["dni"]=int(input("Ingrese su dni: "))

#convertir diccionario en lista

listdic1=list(dic1)
print("El diccionario convertido en lista se ve así: {} y verificamos el tipo de dato que resulta en: {}".format(listdic1,type(listdic1)))

#agregar un key adicional con el nombre profesion

dic1["profesion"]=input("Ingrese la profesión: ")

#eliminar el key dni y mostar el nuevo diccionario

del dic1["dni"]
print("El diccionario ahora resultará en: {}".format(dic1))