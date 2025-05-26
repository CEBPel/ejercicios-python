'''
🧾 1. Calculadora de Propina en un Restaurante
Objetivo: Calcular cuánto debe pagar cada persona, incluyendo propina.

Descripción:

Pide al usuario el total de la cuenta.

Pregunta cuántas personas van a pagar.

Pregunta qué porcentaje de propina quiere dejar (por ejemplo, 10% o 15%).

Muestra el total con propina y cuánto debe pagar cada persona.

Pistas: Usa operadores aritméticos y float.
'''

while True:
    try:
        totalCuenta = float(input("Ingrese el total a pagar: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido.")

while True:
    try:
        print("Cantidad de Personas por pagar:")
        cantPersonas = int(input())
        break
    except ValueError:
        print("Error: debe ingresar una cantidad válido.")

while True:
    try:
        print("Porcentaje de propina:")
        propinaPorcentaje = int(input())
        break
    except ValueError:
        print("Ingrese un porcentaje valido, 1 al 100")

porcentaje = propinaPorcentaje / 100
propina = totalCuenta * porcentaje
totalCuenta = totalCuenta + propina
pagoPorPersona = totalCuenta / cantPersonas

print(f"Total a pagar + propina: {totalCuenta}\n Pago por cada persona: {pagoPorPersona}")



    
    






