import numpy as np
print("+++++Atributos de arreglos en numpy+++++")
np.random.seed(0)
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

# print("El primero es {} el segundo es {} y el tercero es {}".format(x1, x2, x3))
print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("dtype:", x3.dtype)

# otros atributos como itemsize que te da el tamaño en bytes de cada elemento del arreglo
# y nbytes que te da el tamaño en bytes de todo el arreglo
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")

# generalmente, nbytes es igual a itemzise por el zise

"""Array indexing:
Accediendo a elementos singulares del arreglo"""
print("+++++Accediendo a elementos del arreglo+++++")
print(x1)
print(x1[1])
print(x1[0])
print(x1[4])
print(x1[-1])

# sirve para arreglos de varias dimensiones:
print(x2)
print("++++++++++++")
print(x2[1])
print("++++++++++++")
print(x2[0,0])
print("++++++++++++")
print(x2[1,-1])

#modificamos un valor
x2[0,0] = 12
print(x2)

# recordar que los arreglos de NumPy tienen un tipo estandarizado, es decir
# no puedes insertar un float en estos arreglos pues será transformada:
print(x1)
x1[1] = 2.71
print(x1)

# Array slicing, haciendo subarreglos:
print("+++++Haciendo subarreglos+++++")
x = np.arange(10)
print(x)
# primeros 5 elementos
print(x[:5])
# elementos despues del 5
print(x[5:])
# cada otro elemento
print(x[::2])
# cada otro elemento empezando por el indice 1
print(x[1::2])
# todos los elementos al revez
print(x[::-1])
# cada otro elemento al revez desde el indice 5
print(x[5::-2])
print("+++++++++++")
# subarreglos multidimensionales
print(x2)
# dos filas, tres columnas
print(x2[:2, :3])
# todas las filas, cada otras columna
print(x2[:3, ::2])
# podemos revertir un arreglo con subarreglos:
print(x2[::-1, ::-1])

# Accediendo a filas y columnas
print(x2[:, 0]) # primera columna de x2
print(x2[0, :]) # primera fila de x2
print(x2[0]) # equivalente a x2[0, :]

"""Los subarreglos no son copias:"""
print("+++++IMPORTANTE+++++")
print(x2)
# tomamos un subarreglo de x2
x2_sub = x2[:2, :2]
print(x2_sub)
# si lo modificamos, veremos que el arreglo original tambien cambiará
x2_sub[0, 0] = 99
print(x2_sub)
print(x2)
# esta herramienta es bastante util
# aun así podemos hacer copias con .copy()
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)
print(x2)
