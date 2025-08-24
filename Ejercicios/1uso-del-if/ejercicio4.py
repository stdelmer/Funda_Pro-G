"""Escribir un programa que solicite el ingreso de un número, y luego
informe si el mismo es positivo, negativo ó neutro"""
numero = int(input("Ingrese un numero: "))
if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero == 0:
    print(f"El numero {numero} es neutro")
else:
    print(f"El numero {numero} es negativo")