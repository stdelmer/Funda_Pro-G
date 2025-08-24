"""
Escribir una función que reciba un mes y un año; y devuelva la cantidad de días
del mes, considerando los años bisiestos.
Tenga en cuenta que un año bisiesto es aquel divisible por 4, salvo que sea
divisible por 100, en cuyo caso también debe ser divisible por 400.
"""
def validar_dia():
    print("Ingrese un dia aleotorio entre 1 y 365\n")
    dia = int(input("Ingrese el dia aleatorio: "))
    while dia < 1 :
        print("¡¡¡Numero fuera de rango , Vuelva ha intentarlo¡¡¡")
        dia = int(input("Ingrese el dia aleatorio: "))
    return dia

def validar_milenio():
    print("Ingrese un año aleatorio mayor a 1 \n")
    milenio = int(input("Ingrese el año en el que quiere estar: "))
    while milenio < 1 :
        print("¡¡¡Numero fuera de rango , Vuelva ha intentarlo¡¡¡")
        milenio = int(input("Ingrese el año aleatorio: "))
    return milenio

def total_dias_milenio(dia, milenio):
    milenios_pasados = cant_milenios_pasados(milenio)
    #print(f"La cantidad de milenios pasados es {milenios_pasados}")
    cant_bisiesto = cant_bisiestos(milenio, milenios_pasados)
    #print(f"La cantidad de bisiestos es {cant_bisiesto}")
    #Le restamos el año en que estamos(-1)
    milenio_total = milenios_totales(milenio, milenios_pasados)
    #print(f"La cantidad de milenios  acumulados por los milenios bisiestos es {milenios_pasados}")
    dias_totales =  milenio_total * 365 + cant_bisiesto + dia
    return dias_totales

def milenios_totales(milenio, milenios_pasados):
    milenio_totales = milenio - milenios_pasados -1
    return milenio_totales

def cant_bisiestos(milenio, milenios_pasados):
    cant_bisiesto = int((milenio - milenios_pasados) / 4)
    return cant_bisiesto

def devolver_cant_bisiestos(milenio):
    milenio_pasado = cant_milenios_pasados(milenio)
    total_bisiestos = cant_bisiestos(milenio, milenio_pasado)
    return total_bisiestos

def cant_milenios_pasados(milenio):
    milenios_pasados = int(milenio / (365 *4))
    return milenios_pasados

def calcular_mes(dia): 
    dia_mes = dia 
    if dia_mes >= 0 and dia_mes <= 31:
        nombre_mes = "Enero"
    elif dia_mes > 31 and dia_mes <= 60:
        nombre_mes = "Febrero"
    elif dia_mes > 60 and dia_mes <= 91:
        nombre_mes = "Marzo"
    elif dia_mes > 91 and dia_mes <= 121:
        nombre_mes = "Abril"
    elif dia_mes > 121 and dia_mes <= 152:
        nombre_mes = "Mayo"
    elif dia_mes > 152 and dia_mes <= 182 :
        nombre_mes = "Junio"
    elif dia_mes > 182 and dia_mes <= 213:
        nombre_mes = "Julio"
    elif dia_mes > 213 and dia_mes <= 244:
        nombre_mes = "Agosto"
    elif dia_mes > 244 and dia_mes <= 274:
        nombre_mes = "Septiembre"
    elif dia_mes > 274 and dia_mes <= 305:
        nombre_mes = "Octubre"
    elif dia_mes > 305 and dia_mes <= 335:
        nombre_mes = "Noviembre"
    else:
        nombre_mes = "Diciembre"

    return nombre_mes

def milenio_actual_bisiesto(milenio):
    return milenio % 4 == 0
        
def calcular_dia(dias_totales):
    dia_semana = dias_totales % 7
    if dia_semana == 1 :
        resultado = "Lunes"
    elif dia_semana == 2:
        resultado = "Martes"
    elif dia_semana == 3:
        resultado = "Miercoles"
    elif dia_semana == 4:
        resultado = "Jueves"
    elif dia_semana == 5:
        resultado = "Viernes"
    elif dia_semana == 6:
        resultado = "Sabado"
    else :
        resultado = "Domingo"
    return resultado
    
def main():
    print("¡¡¡Calcular que dia cae con un dia del mes y año ¡¡¡")
    #Y yo pensaba que el primer dia es lunes por eso el dominguo(Calendarios)
    print("Suponiendo que el primer dia es 0 y es un Dominguo \n")
    dia =  validar_dia()
    milenio = validar_milenio()
    total_dias = total_dias_milenio(dia, milenio)
    #total_bisiestos = devolver_cant_bisiestos(milenio)
    mes = calcular_mes(dia)
    dia_semana = calcular_dia(total_dias)
    print(f"El dia escogido {dia}, mes {mes} con el año {milenio} es un:  \n{dia_semana}")

main()