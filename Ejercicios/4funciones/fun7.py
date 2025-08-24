"""
Tomá la solución del ejercicio anterior y analizá si elegiste el cliclo adecuado, y si
estás evitando realizar ciclos innecesarios.
Por ejemplo, algunas preguntas que te podrías hacer son:
a) Con sólo encontrar un divisor del número a evaluar distinto a uno y a sí
mismo, ya puedo afirmar que el número no es primo, tiene sentido seguir
evaluando más divisores?
False ,porque el caso borde es cuando sea igual al numero
b) Teniendo en cuenta que todo número par a excepción del 2, no es primo,
tiene sentido seguir en un ciclo, si al calcular el resto de la división del número a
evaluar por 2, el resultado es cero?
False, porque ya encontramos un divisor
c) Puedo encontrar un divisor del número a evaluar que sea mayor al número a
evaluar dividido 2?
False,  divisor <= dividendo/q y en este caso dividendo/q = dividendo/2
Modificá la función escrita en el punto anterior, para que tenga en cuenta las
situaciones planteadas.
"""
def encontrar_divisor(numero):
    elemento = 2
    escope = 1
    divisor = None
    while escope == 1 and numero > 0 and elemento <= numero/2:
        if numero % elemento == 0 :
            divisor = elemento
            escope = 0
        elemento += 1
    return divisor
def evaluar_divisor(divisor):
    if divisor:
        devolver = divisor
    else:
        devolver = None
    return devolver
def main():
    print("¡¡¡Calcular un divisor del numero¡¡¡")
    numero = int(input("Ingrese un numero entero:\n"))
    divisor = encontrar_divisor(numero)
    resultado = evaluar_divisor(divisor)
    print(f"La respuesta es: \n{resultado}")

main()