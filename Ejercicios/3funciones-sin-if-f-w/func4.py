"""
Escribir una función que reciba a través de sus parámetros, la base y la altura de
un rectángulo y devuelva, el perímetro y la superficie, respetando este orden.
"""
#Una funcion solo debe hacer una cosa a la ves
#Validamos que el numero sea positivo

def calcular_perimetro(base, altura):
    perimetro = 2 * (base + altura) 
    return perimetro

def calcular_superficie(base, altura):
    superficie = base * altura
    return superficie
"""
def validar_base():
    base = int(input("Ingrese el valor de la base del rectangulo: \n"))
    while base < 0 :
        print("¡¡¡Valor no valido intentelo de nuevo¡¡¡")
        base = float(input("Ingrese el valor de la base del rectangulo: \n"))
    return base

def validar_altura():
    altura = float(input("Ingrese el valor de la altura del rectangulo: \n"))
    while altura < 0 :
        print("¡¡¡Valor no valido intentelo de nuevo¡¡¡")
        altura = float(input("Ingrese el valor de la altura del rectangulo: \n"))
    return altura
"""
def main():
    print("Calcular perimetro y area de un rectangulo\n")
    base = float(input("Ingrese el valor de la base del rectangulo: \n"))
    altura = float(input("Ingrese el valor de la altura del rectangulo: \n"))
    area = calcular_superficie(base, altura)
    perimetro = calcular_perimetro(base, altura)
    print(f"El perimetro es: {perimetro} \n")
    print(f"El area es {area}")

main()