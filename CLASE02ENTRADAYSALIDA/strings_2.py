"""mas usos para los strings"""

#replace devuelve una copia a la cual se ha cambiado un caracter por otro nuevo
str1 = "Hola mi nombre es Nihho pero me puedes llamar Nihho11"

str1.replace("Hola","Buenas")

print(str1.replace("Hola","Buenas"))

str2 = str1.replace(str1[8:14],"nickname")
print(str2)

#strip, rstrip y lstrip quita ciertos valores: mirar el ejemplo

str3= "            banana             "

print("la fruta {} es mi favorita".format(str3.rstrip()))

str4=",,,,,qsssqssw.,..,banana,.qsqsq,..wwwww"

print(str4.strip(",.qsw"))

"""SPLIT"""
str5="Este es el metodo más basado de python"

x=str5.split()

print(x)

print("XD".join(x))
