"""
 Escribir una función que reciba un valor y calcule el factorial del mismo. Si no se
puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo
contrario deberá devolver el valor calculado.
"""
# Se bdesconoce el numero
# se puede calcular el factorial de un numero negativo es si 
# Yo lo hare para numeros mayores a 0 y enteros 
# Sabemos cuantas veces iterar no (while)
def validar_numero():
    numero = int(input("Ingrese un numero: "))
    if numero > 0 :
        numero = numero
    else:
        numero = 0
    return numero

def factorial_iterativo(numero):
    resultado = 1
    while numero > 0 :
        resultado *= numero
        numero -= 1
    return resultado

def main():
    print("¡¡¡Calcular el factorial¡¡¡")
    numero = validar_numero()
    factorial = factorial_iterativo(numero)
    print(f"El factorial de {numero} es: \n{factorial}")

main()