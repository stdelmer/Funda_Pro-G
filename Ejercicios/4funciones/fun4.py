"""
Escribir una función que reciba un valor n, entero, y devuelva la suma de los
valores entre 0 y n.
"""
#no sabemos cuantas veces iterar (while)
def suma_valores(numero):
    suma = 0
    while numero > 0:
        suma += numero
        numero -= 1
    return suma
def suma_recursiva(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma_recursiva(numero - 1)
def main():
    print("¡¡¡Suma de 0 hasta El numero que usted escoga¡¡¡")
    numero = int(input("Ingrese un numero al cual le quiere hallar su sumatoria desde cero : \n"))
    suma_total = suma_valores(numero)
    #suma = suma_recursiva(numero)
    #print(f"La suma total recursivamente es {suma}\n")
    print(f"El resultado es : {suma_total}")

main()