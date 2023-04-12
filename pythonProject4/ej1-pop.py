"""uso de pop en python
elimina un item en la posición dada
se puede usar sin seleccionar la posición"""

paises=["Uruguay","Perú","Chile","Argentina"]

#borra el ultimo valor si no indicas nada
paises.pop()

print("Los valores de mi lista actual son: {}".format(paises))
print("El tamaño de la lista es: {}".format(len(paises)))

paises2=["Uruguay","Perú","Chile","Argentina"]

paises2.pop(2)

print(paises2)
