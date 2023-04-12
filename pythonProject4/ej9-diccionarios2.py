"""diccionarios
usando sorted para:
obteniendo solamente los valores de los key o columnas"""

diccionario={"nombre":"Mysql","tipo":"BD Relacional"}

keys=sorted(diccionario)
print(diccionario)
print(keys)

"""convertir diccionario a lista"""

varDiccionario={"nombre":"Mysql","tipo":"BD Relacional"}

list(varDiccionario)

print("mi diccionario convertido es el siguiente: {}".format(list(varDiccionario)))

"""Uso de values para mostrar valores en lugar de keys"""

valores= list(varDiccionario.values())
print(valores)

keys=list(varDiccionario.keys())
print(keys)
"""crea una lista de pares tipo (key,item)"""
lista_convertida=varDiccionario.items()
print(lista_convertida)