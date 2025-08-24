"""
Un palíndromo es una palabra o frase que se puede leer de igual modo en ambos
sentidos. Por ejemplo: Oso - Ana - Oso baboso - Arriba la birra
Escribir una función que reciba una frase que podría estar compuesta por una o
más palabras; y devuelva True, si se trata de un palíndromo, de lo contrario,
deberá devolver False.
"""
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    palabra_invertida = invertir_palabra(palabra)
    if palabra_invertida  == list(palabra.replace(" ", "")):
       valor = True
    else:
        valor = False
    return valor        
    
def invertir_palabra(palabra):
    indice = 0
    lista_palabra = list(palabra)
    palabra_invertida = []
    while indice < len(palabra):
        palabra_invertida.insert(indice, lista_palabra[len(palabra) - indice -1])
        indice += 1
    return palabra_invertida

def imprimir_es_palindromo(es_palindromo, palabra):
    if es_palindromo:
        print(f"La palabra {palabra} es palindroma")
    else:
        print(f"La palabra {palabra} no es palindroma")

def main():
    print("¡¡¡Calcular si una palabra es palindroma¡¡¡")
    print("Los espacios de las palabras no cuentan")
    palabra = input("Ingrese una Palabra: ")
    valor = es_palindromo(palabra)
    imprimir_es_palindromo(valor, palabra)

main()