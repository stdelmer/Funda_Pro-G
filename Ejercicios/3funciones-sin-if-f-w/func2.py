from math import pi
"""
Escribir una función que reciba por medio de un parámetro, el radio de un círculo
y retorne su área.
"""
def calcular_area(radio):
    return pi*radio*radio

def main():
    print("¡¡¡Calcular Area¡¡¡")
    parametro = float(input("Ingrese el radio de una circunferencia: "))
    print(f"EL area de la circunferencia es {calcular_area(parametro)}")

main()