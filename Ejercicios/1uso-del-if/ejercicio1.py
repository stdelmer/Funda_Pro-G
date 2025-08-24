"""Escribir un programa que solicite el ingreso de dos números y luego
informe cuál es el mayor de los números ingresados.
Suponer que siempre los números ingresados serán distintos.
"""
numero1 = int(input("Ingrese un primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
if numero1 > numero2 :
    print(f"El numero mayor entre {numero1} y {numero2} es {numero1}")
else:
    print(f"El numero mayor entre {numero1} y {numero2} es {numero2}")