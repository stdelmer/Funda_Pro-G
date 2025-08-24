"""
Escribir una función que reciba como primer parámetro, la velocidad de
desplazamiento de un objeto; y como segundo parámetro, el tiempo durante el
cual se desplazó. La función debe devolver la distancia recorrida.
Tener en cuenta que: velocidad = distancia / tiempo
"""
#movimiento rectilinio uniforme(MRU) v=d/t
def calcular_desplazamiento(velocidad, tiempo):
    return velocidad * tiempo
"""
def validar_tiempo():
    tiempo = float(input("Ingrese la cantidad de tiempo(s) de vuelo del objeto: \n"))
    while tiempo < 0 :
        print("¡¡¡El tiempo no puede ser negativo¡¡¡")
        tiempo = float(input("Ingrese la cantidad de tiempo de vuelo del objeto(segundos): \n"))
    return tiempo
"""
def main():
    print("¡¡¡Movimiento Rectilineo Uniforme(MRU) o velocidad = constante¡¡¡")
    velocidad = float(input("ingrese la velocidad(m/s) del objeto: \n"))
    tiempo = tiempo = float(input("Ingrese la cantidad de tiempo(s) de vuelo del objeto: \n"))
    desplazamiento = calcular_desplazamiento(velocidad, tiempo)
    print(f"El desplazamiento del objeto es de  {desplazamiento} metros")
main()