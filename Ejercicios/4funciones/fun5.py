"""
Escribir una función que reciba las coordenadas de dos puntos en una recta, y
devuelva la pendiente de la misma. Tener en cuenta que: la pendiente ó m =
(y2 - y1)/(x2 - x1), donde (x1, y1) y (x2, y2), serán las coordenadas del primer
y segundo punto, respectivamente.
"""
def hallar_pendiente(abcisa1, abcisa2, ordenada1, ordenada2):
    resta_ordenadas = ordenada2 -ordenada1
    resta_abcisas = abcisa2 -abcisa1
    if resta_abcisas == 0:
        pendiente = abcisa1
    elif resta_ordenadas == 0:
        pendiente = ordenada1
    else :
        pendiente = resta_ordenadas / resta_abcisas
    return pendiente
def ecuacion_recta(abcisa, ordenada, pendiente):
    recta = -1 * pendiente * abcisa + ordenada
    return recta

def main():
    print("¡¡¡Vamos a calcular la ecuacion de la recta¡¡¡")
    x1 = int(input("Ingrese la abcisa del primer punto:: "))
    y1 = int(input("Ingrese la ordenada del primer punto: "))
    x2 = int(input("Ingrese la abcisa del segundo punto: "))
    y2 = int(input("Ingrese la ordenada del segundo punto: "))
    pendiente = hallar_pendiente(x1, x2, y1, y2)
    recta = ecuacion_recta(x1, y1, pendiente)
    print(f"La ecuacion de la recta es : \nY = {pendiente}X + {recta}")

main()