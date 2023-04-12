#crear diccionario
dic1={"nombre":"Eduardo","edad":22,"salario":3000,"edad":22}
print("Mi diccionario 1 es: {}".format(dic1))
#convertirlo a lista
list(dic1)
print("Mi diccionario convertido en lista es: {}".format(list(dic1)))
#agregar un nuevo key
dic1["dni"]=83294483

#eliminar un key y su valor
del dic1["edad"]
print("El diccionario ahora queda así: {}".format(dic1))

#convertir en lista
print("El diccionario convertido en lista es {} y tiene los tipos de dato {}".format(list(dic1),type(list(dic1))))

#crear diccionario con mismos valores

dic2={}
dic2["key1"]="sí"
print(dic2)

#diccionario con 6 departamentos

dicdep={"dep1":"Tumbes", "dep2":"Lambayeque", "dep3":"Lima", "dep4":"Madre de Dios", "dep5":"Piura", "dep6":"Cuzco"}

del dicdep["dep2"]

print(dicdep)

#ingresar carrera

dic1["carrera"]="Física"

print(dic1)

