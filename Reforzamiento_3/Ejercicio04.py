"""Crea una función que al ingresar dos números por parámetro mostrará
todos los números que hay entre ellos (Usar la función una vez y
mostrar el resultado por consola). Los números serán ingresados por
consola por el usuario."""

def num_en_medio(a, b):
    list1 = []
    if b>(a+1):
        for numero in range(b-a-1):
            list1.append(numero+a+1)
        return list1
    elif a>(b+1):
        for numero in range(a-b-1):
            list1.append(numero+b+1)
        return list1
    else:
        return "¡No hay numeros enteros entre esos dos numeros!"


num1 = int(float(input("Ingrese un número: ")))
num2 = int(float(input("Ingrese otro número: ")))

print(num_en_medio(num1,num2))

