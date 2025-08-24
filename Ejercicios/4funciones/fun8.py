"""
Escribir una función que reciba dos valores enteros, y devuelva el máximo
común divisor entre ambos números.
Recordemos que se define el máximo común divisor (MCD) de dos o más
números enteros al mayor número entero que los divide sin dejar resto alguno.
Te sugerimos que antes de programar la solución te hagas preguntas del tipo a
las planteadas en en el ejercicio anterior
"""
def maximo_comun_divisor(numero1, numero2):
    elemento =1
    divisor = 1
    while numero2 > 0 and numero1 > 0 and elemento < numero1 + 1 and elemento <= numero2 + 1:
        if numero1 % elemento == 0 and numero2 % elemento == 0:
            divisor = elemento
        elemento += 1
    return divisor

def main():
    print("¡¡¡Calcular MCD de dos numeros y si no tiene divisor(None)¡¡¡")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    divisor = maximo_comun_divisor(numero1, numero2)
    print(f"El Maximo comun divisor es : \n{divisor}")

main()