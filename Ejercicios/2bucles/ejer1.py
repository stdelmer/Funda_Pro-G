"""Escribir un programa que solicite el ingreso de un número y luego
calcule e informe el factorial del número ingresado."""
#sabemos cual es el numero y cuantas veces iterar (for)
print("Calcular Factorial")
numero = int(input("Ingrese un numero entero: "))
factorial = 1
for elemento in range(1,numero,1):
    factorial *= (elemento +1)
print(f"El factorial de {numero} es {factorial}")