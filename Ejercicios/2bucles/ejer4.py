"""
Mostrar en forma descendente, los número pares entre 100 y 0
inclusive.
"""
#sabemos cuantas iteraciones y no hay una condicion de corte (for)
print("Los numeros pares del 100 al 0 (inclusive):\n") 
for elemento in range(0, 101):
    if elemento % 2 == 0:
        print(f"{100 - elemento} ")
    
