'''
🕒 2. Calculadora de Tiempo de Viaje
Objetivo: Estimar cuánto tiempo tomará un viaje.

Descripción:

Pide al usuario la distancia total en kilómetros.

Pide la velocidad promedio del vehículo (en km/h).

Calcula cuántas horas tomará llegar (tiempo = distancia / velocidad).

Muestra el tiempo estimado en horas y minutos (extra: convierte los decimales a minutos).

Pistas: Puedes usar int() y round() para redondear.
'''


while True:
    try:
        distancia = float(input("Ingrese la distancia en km: "))

        if distancia <= 0:
            raise  ValueError("La distancia no puede ser 0 o negativo")
        
        break
    except ValueError as e:
        print(f"Error: {e}")

while True:
    try:
        velocidad = float(input("Ingrese la velocidad promedio del vehiculo: "))
        if velocidad <= 0:
            raise ValueError("La velocidad no puede ser 0 o negativo.")
        break
    except ValueError as e:
        print(f"Error: {e}.")

tiempo = round(distancia / velocidad, 3)

horas = int(tiempo)
minutos = round((tiempo - horas) * 60)

print(f"Tiempo estimado del viaje: {horas}:{minutos}")
