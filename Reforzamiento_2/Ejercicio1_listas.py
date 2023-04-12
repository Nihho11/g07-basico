#crea lista con 6 objetos y mostrar

lista1=["Mecánica Clásica I","Física Computacional I","Física Computacional II","Electromagnetismo I", "Electromagnetismo II", "Introducción a la Sismología"]

print("Mi lista 1 es: {}".format(lista1))
#agregar 4 objetos

lista1.append("Excel I")
lista1.append("Python Básico")
lista1.append("SQL Básico")
lista1.append("Mecánica Cuántica I")

#eliminar 2 objetos por valor

lista1.remove("Mecánica Clásica I")
lista1.remove("Electromagnetismo I")

#lista con objetos agregados

print("Mi lista actualizada es: {}".format(lista1))

#invertir lista

lista1.reverse()

print("Mi lista inveritda es: {}".format(lista1))

#mostrar cantidad de items en lista

print("la cantidad de objetos en mi lista es: {}".format(len(lista1)))

#mostrar veces que se repite un curso

lista1.append("SQL Básico")

print("la cantidad de veces que se repite el curso SQL Básico es: {}".format(lista1.count("SQL Básico")))

#borrar primer item de la lista
lista1.pop(0)
print(lista1)

#nueva lista
lista2=[]
lista2.append(1)
lista2.append(2)
lista2.append(3)
lista2.append(1.2)
lista2.append(5.4)
lista2.append(2.21)
lista2.append("Hola")
lista2.append("Sí")
lista2.append("No")
#sumar listas y mostrar
print("Las listas sumadas nos da esta lista: {}".format(lista1+lista2))

#10. lista con métodos de orden
lista3=[32,11,4,12,18,20,26,1,3]

#crear lista e imprimir el penultimo e ultimo valor
lista4=[2.3,3.3,3.14,True,False,10.1]
print("El penúltimo y último valor son: {} y {}".format(lista4[-2],lista4[-1]))

#tipos de datos en la lista creada
for i in lista4:
    print("en la lista 4, el dato {} es del tipo {}".format(i,type(i)))
#eliminar todos los elementos
for i in range(len(lista4)):
    lista4.pop()
print("el estado de la lista es:", lista4)

lista4=[2.3,3.3,3.14,True,False,10.1]
#eliminar 2 elmentos por indice

lista4.pop(2)
lista4.pop(3)

print("la lista con valores eliminados es: {}".format(lista4))

#crear lista con los 100 primeros enteros

listaent=[]

for i in range(100):
    listaent.append(i)

print(listaent)

#los datos entre 10 y 35

print("los datos entre la posición 10 y 35 son {}".format(listaent[10:36]))

#lista con numeros cuadrados

listacuad=[]

for i in range(10):
    listacuad.append(i**2)

print("la lista de los primero 10 mumeros cuadrados es: {}".format(listacuad))

#lista primeros 15 numeros impares

listaimp=[]
for i in range(15):
    listaimp.append(2*i+1)
for i in range(3):
    listaimp.append(3.0)

listaimp.insert(3,"Hola")
# ###considerando que existe una posición 0, esta es la posición 3

del listaimp[3]
print(listaimp)

#crear lista vacía
listasumymed=[]

for i in range(10):
    listasumymed.append(input("inserte el número {}:".format(i+1)))

for i in range(10):
    listasumymed[i]=int(listasumymed[i])

print("la suma de los valores y el promedio de estos son: {} y {}".format(sum(listasumymed),sum(listasumymed)/len(listasumymed)))