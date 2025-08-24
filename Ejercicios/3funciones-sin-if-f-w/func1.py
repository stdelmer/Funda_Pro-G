from math import pi
#El modulo math de python ya es una libreria que por lo general ya viene con python
"""
Ejercicios - Declaración de Funciones Simples
(Sin uso de condicionales y ciclos)
Para la solución de los siguientes ejercicios, no debes imprimir resultados dentro de
las funciones que escribas. Los resultados deben ser devueltos mediante el return de
la función.
Luego de escribir cada función, probala, invocándola desde el bloque principal del
programa, pasándole distintos valores para que la prueba tenga en cuenta varias
alternativas y así estar seguro que funciona adecuadamente.
1. Escribir una función que reciba a través de un parámetro, el radio de una
circunferencia y retorne su longitud.
"""
#faltan muchas cosas dentro de ellas una es validar que sea un numero positivo
def long_circun(radio):
    return 2*pi*radio
def main():
    parametro = int(input("Ingrese el radio de una circunferencia: "))
    print(f"La longitud de la circunferencia es {long_circun(parametro)} ")
main()