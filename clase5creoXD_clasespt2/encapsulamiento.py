"""POO en Python"""
"""Encapsulamiento"""

class A:
    def __init__(self): #definimos su constructor
        """Encapsulamiento"""
        self.inicial = False
        self._contador = 0  #Definiendo mi atributo privado, es decir no puede ser modificado, por el guion la variable no se debe alterar, editar. se puede pero no deberia

    def incrementa(self):
        self._contador += 1

    def cuenta(self):
        return self._contador


class B():
    """Encapsulamiento"""
    def __init__(self):
        self.inicial = True
        self.__contador = 0    #Definiendo mi atributo privado, NO ES POSIBLE ALTERAR ESTA VARIABLE

    def incrementa(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador


varA = A()
varA._contador
varA.inicial = True

varA.incrementa()
varA.incrementa()

print("Contador A: {}". format(varA._contador))
print("Valor inicial de A: {}".format(varA.inicial))

varB = B()
varB.inicial = False

for i in range(4):
    varB.incrementa()

print("Valor del contador B es: {}".format(varB.cuenta()))
print("Valor inicial de B: {}".format(varB.inicial))

# no es posible invocar a una variable pues el encapsulamiento es fuerte por los dos guines abajo previos
# print("Intentaré llamar  un variable con encapsulamiento fuerte XDDXDXD que noob: {}".format(varB.__contador))

