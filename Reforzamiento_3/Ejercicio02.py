"""Crear una clase en python que contenga un método que revierta una
cadena de palabras
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seghimos Pythonista Hola" """


class Revertir:
    def revertire(self,cadena):
        cadena_lista = cadena.split()
        cadena_lista.reverse()
        self.cadena_revertida = " ".join(cadena_lista)
        return self.cadena_revertida


cadena_ej = input("Ingresa la oración que quieres invertir: ")

cadena1 = Revertir()

print(cadena1.revertire(cadena_ej))

