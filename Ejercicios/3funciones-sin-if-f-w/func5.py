"""
Escribir una función que reciba como parámetro una temperatura en grados
Fahrenheit y devuelva el valor en Celsius. Tener en cuenta que: F = (C * 1,8) +
32
"""
#Los grados centigrados pueden ser positivos o negativos
def celcius_fahrenheit(celcius):
    fahrenheit = (celcius *18 / 10) + 32
    return fahrenheit

def main():
    print("Convertir celcius a fahrenheit \n")
    celcius = float(input("Cuantos grados celcius  a fahrenheit quiere convertir: \n"))
    fahrenheit = celcius_fahrenheit(celcius)
    print(f"La cantidad de fahrenheit es {fahrenheit}")
main()