"""
Solicitar el ingreso de un número y luego informar si el número
ingresado es un número primo
"""
#si hay una condicion de corte es un while
#Los numeros primos no pueden ser negativos
numero = int(input("Ingrese un numero para evaluar su divisivilidad: "))
contador = 2

while contador != -1 and contador < numero:
    if numero % contador == 0 :
        print("El numero no es primo")
        print(f"Un multiplo es {contador}")
        contador = -1
    else:
        contador += 1
if contador == numero:
    print("El numero es primo")

