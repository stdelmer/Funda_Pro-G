"""
Escribir una función que reciba a través de sus parámetros, dos valores
numéricos, y devuelva True (verdadero), si el primer parámetro es mayor que el
segundo, de lo contrario debe devolver False (falso).
Dale a la función el nombre es_mayor
"""
from unittest import result


def es_impar(numero1, numero2):
    return numero1 > numero2

def main():
    print("¡¡¡Calcular por True o False si un numero es mayor a otro¡¡¡")
    print("Numeros a comparar:\n")
    numero1 = int(input("Ingrese el primero numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    resultado = es_impar(numero1, numero2)
    print(f"El Resultado fue de : \n{resultado}")

main()