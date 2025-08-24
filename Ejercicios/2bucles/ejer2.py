"""Escribir un programa que solicite el ingreso de valores numéricos.
El ingreso finalizará cuando el usuario haya ingresado como último
valor, un cero.
Informar el total de los valores acumulados y cuantos valores fueron
ingresados"""
#No sabemos cuantas veces iterar y desconocemos el valor (While)
#\n salto de linea
#contamos el cero exclusive
numero1 = 1
cont = 0
while numero1 != 0:
    numero1 = int(input("Ingrese un numero para ser contado y 0 para terminar: \n"))
    cont +=1
cont -= 1
print(f"La cantidad de veces es {cont}")