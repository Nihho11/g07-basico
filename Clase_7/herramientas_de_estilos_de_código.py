""" Usar flake8 desde el Command Prompt para correxiónes del código
se utiliza para que el código sea legible y fácil de entender"""

# un ejemplo de una clase pasada:
ingenierias = ["Software", "Sistemas", "Industrial", "Química",
               20, 40, "Mecánica"]

print("El tamaño de mi lista es: {}".format(len(ingenierias)))
i = 1
for ingenieria in ingenierias:
    print(ingenieria)
    try:
        print("Bienvenido Ing. " + ingenieria)
    except TypeError:
        print("Has ingresado un valor incorrecto")
    print("Esta es la vuelta número {}".format(i))
    i = i+1
