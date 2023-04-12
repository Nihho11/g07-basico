a1 = int(input("Valor1: "))
a2 = int(input("Valor2: "))
a3 = int(input("Valor3: "))


def media(x):
    return sum(x)/len(x)

lista1 = []

lista1.append(a1)
lista1.append(a2)
lista1.append(a3)

print("La media de los valores {}, {} y {} es: {}".format(a1,a2,a3,media(lista1)))

print(lista1)