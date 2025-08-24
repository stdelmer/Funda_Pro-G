"""
Escribir una función que reciba a través de sus parámetros, dos valores enteros,
y devuelva True, si el primer parámetro es múltiplo del segundo, de lo contrario
debe devolver False. No te preocupes por el caso que uno ó ambos valores
recibidos sea igual a cero.
Dale a la función el es_multiplo_de.
"""
def es_multiplo_de(valor1, valor2):
    return valor1 % valor2 == 0

def main():
    print("¡¡¡Comaparar si son multiplos dos numeros¡¡¡")
    print("Si el primer numero es multiplo del segundo (True) caso contrario False: \n")
    valor1 = int(input("Ingrese el primer valor a comparar:\n"))
    valor2 = int(input("Ingrese el segundo valor a comparar:\n"))
    resultado = es_multiplo_de(valor1, valor2)
    print(f"El resultado fue :\n{resultado}")

main()