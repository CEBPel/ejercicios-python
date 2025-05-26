'''
📆 4. Conversor de Edad Humana a Edad Canina
Objetivo: Convertir edad humana a edad de perro con una regla más realista.

Descripción:

Pide la edad del usuario.

Si la edad es menor o igual a 2, cada año humano equivale a 10.5 años perro.

Si es mayor a 2, los primeros 2 años valen 10.5 cada uno y el resto 4 años perro por año humano.

Muestra la edad equivalente en años perro.

Pistas: Necesitas if, operadores, y algo de lógica.
'''

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Error: Valor invalido, intenlo nuevamente.")

if edad <= 2:
    edad *= 10.5
else:
    edad = ((edad - 2) * 4) + 21


print(f"Su edad perruna: {edad}")