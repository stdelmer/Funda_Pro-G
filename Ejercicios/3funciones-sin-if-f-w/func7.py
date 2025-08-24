"""
Escribir una función que reciba una cantidad de segundos, y devuelva el
equivalente en días, horas, minutos, segundos. Devolver los valores en el orden
indicado.
"""
"""
def validar_segundos():
    segundos = int(input("Ingrese la cantidad de segundos: \n"))
    while segundos < 0:
        print("La cantidad de segundos no puede ser negativa¡¡¡")
        segundos = int(input("Ingrese la cantidad de segundos : \n"))
    return segundos
"""
def total_segundos_dias(segundos):
    dias = segundos /(60 * 60 * 24)
    return int(dias)
def main():
    total_segundos = int(input("Ingrese la cantidad de segundos: \n"))
    dias = int(total_segundos_dias(total_segundos))
    total_segundos %= 60*60*24
    horas = int(total_segundos/(60 * 60))
    total_segundos %= 60*60
    minutos = int(total_segundos/(60))
    total_segundos %= 60
    segundos = total_segundos
    print("La conversion es : \n")
    print(f"dias({dias}) horas({horas}), minutos({minutos}) y los segundos({segundos})")
main()