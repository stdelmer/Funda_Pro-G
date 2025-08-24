"""
Escribir una función que reciba un número y devuelva un valor booleano
indicando si el número recibido es ó no primo.
"""
def es_primo(numero):
    elemento = 2
    escope = 1
    while escope == 1 and numero > 0 and elemento != numero and numero != 2:
        if numero % elemento == 0 :
            escope = 0
        elemento += 1
    return escope == 1

def main():
    print("¡¡¡Calcular el booleano de un numero si es primo(True) caso contrario (False) ¡¡¡")
    numero = int(input("Ingrese un numero entero:\n"))
    resultado = es_primo(numero)
    print(f"La respuesta es: \n{resultado}")

main()