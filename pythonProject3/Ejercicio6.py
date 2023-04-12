"""Calcular media de 5 valores"""

#declarar 5 valores
A=[2,3,10,4,6]

#hay una función de numpy en python que ecuentra la media de los valores indicados
#de forma manual se puede encontrar la suma entre la cantidad de valores

media=sum(A)/len(A)

print("La media de los valores {}, {}, {}, {}, {} es {}".format(A[0],A[1],A[2],A[3],A[4],media))