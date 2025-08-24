"""
Escribir una función que reciba un valor en centímetros y devuelva el equivalente
en pulgadas. Tener en cuenta que 1 cm equivale a 0,393701 pulgadas
"""
#Los decimales es con puntos no con coma
#python comete eso error minimo al multiplicar por flotantes
#Esta es la funcion:
def convertir_cm_pulg(centimetros):
    pulguadas = centimetros * (393701/1000000)
    return pulguadas
#Aqui termina la funcion

def main():
    centimetros = centimetros = float(input("Ingrese la cantidad de centimetros: "))
    print(f"La cantida de pulguadas es:\n {centimetros}")

main()