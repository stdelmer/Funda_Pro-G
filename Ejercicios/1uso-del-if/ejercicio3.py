"""Escribir un programa que solicite el ingreso de un número, y luego
indique si el número ingresado es par ó impar. Suponer que el
número ingresado será un número entero.
"""
variable = int(input("Ingrese un numero entero: "))
if variable % 2 == 0:
    print(f"El numero {variable} es par")
else :
    print(f"El numero {variable} es impar")