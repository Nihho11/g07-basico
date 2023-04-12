"""uso de reverse en python
invierte los elemento de una lista"""

lista1=[1,2,3,4,5,6,"Hola","Soy","Eduardo"]
print(lista1)
lista1.reverse()
print(lista1)

listaA=[4,2,23,1,56,3,2,88,34,26,32]
print(listaA)
listaA.sort()
print(listaA)

lista2=["asdasd","a","si","claroquesimiestimadoamigo","puntofortran"]
print(lista2)
def mifun(e):
    return len(e)

lista2.sort(key=mifun)
print(lista2)