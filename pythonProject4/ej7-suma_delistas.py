"""suma de listas"""

edad1=[19,23,32,21,9,20,"Gonzales"]
edad2=[21,30,40,16,20,"Ramirez"]

print("la suma de las listas es: {}".format(edad1+edad2))

"""Listas: Recorrido de listas"""

sueldos = [1000,3000,6000,8000,9000,12000]

print("Tamaño de mi lista: {}".format(len(sueldos)))
sueldosmayores=[]
for i in range(len(sueldos)):
    print(sueldos[i])

for i in sueldos:
    if i>=8000:
        sueldosmayores.append(i)

print(sueldosmayores)