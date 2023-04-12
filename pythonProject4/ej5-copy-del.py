"""uso de copy en python
copia los elementos de la lista
es util pues uno no puede hacer listaB=listaA para crear una nueva lista con los mismos elementos
simplemente va a redirigirte a la misma listaA y no puedes editar la nueva lista sin alterar la anterior"""

lista1=[2,3,4,1,"Jueves"]

print(lista1)

lista2=lista1.copy()

lista2.append("tilin")

print(lista1)


"""uso de del en python
elimina"""
#como comentario pues causa un error al no existir x, esto puede ser una lista también
"""x = "hello"

del x

print(x)"""
