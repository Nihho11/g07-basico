import numpy as np
import array
L = np.array([range(i, i + 3) for i in [2, 4, 6]])
print(L)

# numpy normaliza tus datos:
l1 = np.array([2, 3, 9, 3.14])
print(l1)

# puedes escoger que tipo de dato:

l2 = np.array([2, 3, 9, 3.14], dtype = 'int')
print(l2)

# puedes crear un arreglo de solo 0
lzero = np.zeros(10, dtype = int)
print(lzero)

# crear un arreglo de unos en dos dimensiones
lone = np.ones((3,5), dtype = float)
print(lone)

# un arreglo de un valor
lpi = np.full((6,5), 3.14)
print(lpi)

# un arreglo lleno de una secuencia lineal
# Empezará en 0, terminará en 20 y saltará de 2 en 2
# es similar a la función range()
lsecuencia = np.arange(0, 20, 2)
print(lsecuencia)

# crear un arreglo de 5 valores separados equitativamente entre
# dos valores:
lequit = np.linspace(0, 1, 5)
print(lequit)

# crear un arreglo 3x3 con valores al azar
lrandom = np.random.random((3, 3))
print(lrandom)

# crear un arreglo 3x3 con valores normalmente distribuidos con promedio 0 y desviacion standar 1
lrandommed = np.random.normal(0, 1, (3, 3))
print(lrandommed)

# crear un arreglo con valores al azar en el intervalo [0, 10)
lrandomint = np.random.randint(0, 10, (3, 3))
print(lrandomint)

# matriz identidad
mident = np.eye(3)
print(mident)

# crear un arreglo no iniciado de 3 enteros
# los valores serán lo que exista en la memoria en ese momento
l3 = np.empty(3)
print(l3)