"""
Para la solución de los siguientes ejercicios, no debes imprimir resultados dentro de
las funciones que escribas. Los resultados deben ser devueltos mediante el return de
la función.
Luego de escribir cada función, probala, invocándola desde el bloque principal del
programa, pasándole distintos valores para que la prueba contemple varias
alternativas y así estar seguro que funciona adecuadamente.
1. Escribir una función que reciba el número de un mes, y devuelva el nombre del
mes.
Por ejemplo, si la función recibe un "1", deberá devolver: "Enero"
En caso que el mes recibido no sea válido, deberá devolver "Mes Inválido".
No debe imprimir el nombre, sólo devolver la cadena correspondiente.
"""
#En programacion generalmente no se usa la letra que sigue de la n
def imprimir_mes(numero_mes):
    if numero_mes == 1:
        valor = "Enero"
    elif numero_mes == 2:
        valor = "Febrero"
    elif numero_mes == 3:
        valor = "Marzo"
    elif numero_mes == 4:
        valor = "Abril"
    elif numero_mes == 5:
        valor = "Mayo"
    elif numero_mes == 6:
        valor = "Junio"
    elif numero_mes == 7:
        valor = "Julio"
    elif numero_mes == 8:
        valor = "Agosto"
    elif numero_mes == 9:
        valor = "Septiembre"
    elif numero_mes == 10:
        valor = "Octubre"
    elif numero_mes == 11:
        valor = "Noviembre"
    elif numero_mes == 12:
        valor = "Diciembre"
    else:
        valor = "Mes Invalido"  
    return valor

def main():
    print("¡¡¡los meses del año¡¡¡")
    mes = int(input("Ingresa un mes siendo 1 - enero y 12 - diciembre: "))
    devolvio = imprimir_mes(mes)
    """
    mes1 = 4
    mes2 = 6
    mes3 = 14
    devolvio1 = imprimir_mes(mes1)
    devolvio2 = imprimir_mes(mes2)
    devolvio3 = imprimir_mes(mes3)
    print(f"mes1:{devolvio1}\nmes2: {devolvio2}\nmes3: {devolvio3}")
    """
main()