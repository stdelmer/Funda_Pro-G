"""
Escribir una función que reciba por parámetro, un valor entero, y devuelva True
si el valor recibido es impar; de lo contrario debe devolver False.
Dale a la función el nombre es_impar.
"""
#"Sin condicionales ni bucles lo veo dificil" eso fue lo que dije en un inicio¡¡¡
#pero los operadores de comparacion devuelven un valor booleano
def es_impar(numero):
    return numero %2 != 0
def main():
    print("¡¡¡Ver si es par o impar un numero entero¡¡¡")
    numero = int(input("Ingrese un numero entero: "))
    par_impar = es_impar(numero)
    print(f"si es True es impar si es false es par y el valor devuelto es : \n{par_impar}")
main()
