"""Concepto de listas"""
#crear lista con 10 valores random

lista1=[3,2,5,7,6,6,12,3,0,1]

#llenar otra lista con sus cubos

lista1cub=[]
for i in lista1:
    lista1cub.append(i**3)

#llenar una lista nueva con sus cuadrados

lista1cuad=[]
for i in lista1:
    lista1cuad.append(i**2)

#mostrar de manera inversa la suma de ambas listas

listasum=lista1cub+lista1cuad
listasum.reverse()

print("La suma de ambas listas, invertida resulta en {}".format(listasum))

