"""Ahora, tomá el ejercicio anterior y considera que el usuario podría
ingresar dos veces el mismo número.
"""
numero1 = int(input("Ingrese un primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 > numero2 :
    print(f"El numero mayor entre {numero1} y {numero2} es {numero1}")
elif numero1 == numero2:
    print(f"El numero mayor entre {numero1} y {numero2} no tiene porque son iguales")
else:
    print(f"El numero mayor entre {numero1} y {numero2} es {numero2}")