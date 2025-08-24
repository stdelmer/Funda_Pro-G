"""
El producto de Wallis es una expresión matemática, utilizada para representar el
valor del número Pi, que fue descubierta por John Wallis en 1655 y que
establece que:
pi es la productoria desde i = 1 hasta el infinito de 4((n)^2 /[4{(n)^2} - 1] )
Escribir una función, que reciba por parámetro, el valor más alto a utilizar en el
cálculo (n). La función debe calcular el valor de Pi utilizando la fórmula de Wallis
y devolver el valor de Pi obtenido.
Proba la función, utilizando al menos, como valor de n, 100, 1000 y 10000.
"""
def producto_wallis(numero):
    pi = 1
    indice = 1
    while indice < numero:
        pi *= (2 * indice) /(2 *indice - 1) * (2 * indice ) /(2 * indice   + 1)
        indice += 1
    return pi
def main():
    print("¡¡¡Estimar pi a traves del producto de wallis¡¡¡")
    cota_superior = int(input("Ingrese un numero positivo y entero a la ves: "))
    pi = producto_wallis(cota_superior)
    print(f"El valor de pi es: \n{2*pi}")

main()