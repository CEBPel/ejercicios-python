'''
🛒 5. Mini sistema de descuentos para compras
Objetivo: Calcular cuánto debe pagar un cliente con posibles descuentos.

Descripción:

Pide al usuario el monto total de su compra.

Si la compra es mayor a $100, se aplica un 10% de descuento.

Si es mayor a $200, se aplica un 20% de descuento.

Si es menor a $100, no hay descuento.

Muestra el total a pagar luego del descuento.

Pistas: Usa if/elif/else y operadores de comparación.
'''
while True: 
    try:
        monto_total = float(input("Ingrese el monto total de la compra: "))
        break
    except ValueError:
        print("Error: Valor invalido, intentelo nuevamente.")

if monto_total >= 100 and monto_total <= 200:
    monto_total *= 1.10
    print(f"Descuento del 10%, nuevo monto: {monto_total:.2f}")
elif monto_total > 200:
    monto_total *= 1.20
    print(f"Descuento del 20%, nuevo monto: {monto_total:.2f}")
else:
    print("Sin descuentos.")
