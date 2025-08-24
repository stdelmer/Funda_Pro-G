"""Escribir un programa que solicite el ingreso de tres palabras, y luego
las muestre en orden alfabético. Suponer que las palabras ingresadas
sólo contendrán letras minúsculas.
"""
print("Evaluamos las palabras por la letra que empieza y por la longitud")
palabra1 = input("Ingrese la primera  palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
palabra3 = input("Ingrese la tercera  palabra: ")
if palabra1 >= palabra2 and palabra1 >= palabra3:
    print(f"La palabra {palabra1} es la mayor")
elif palabra2 >= palabra3 and palabra2 >= palabra1 :
    print(f"La palabra {palabra2} es la mayor")
else:
    print(f"La palabra {palabra3} es mayor")