'''
🎢 3. Requisitos para una Montaña Rusa
Objetivo: Verificar si una persona puede subirse a una atracción.

Descripción:

Pide al usuario su edad y estatura en cm.

La persona solo puede subirse si tiene al menos 12 años y mide más de 140 cm.

Imprime si puede o no subir.

Pistas: Usa operadores lógicos (and) y condicionales (if).
'''

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Error: Valor invalido, solo ingrese numeros.")

while True:
    try:
        estatura = int(input("Ingrese su tamaño en cm: "))
        break
    except ValueError:
        print("Error: Valor invalido, vuelva a intentarlo.")

if edad >= 12 and estatura > 140:
    print("Si se puede subir")
else:
    print("No se puede subir")
