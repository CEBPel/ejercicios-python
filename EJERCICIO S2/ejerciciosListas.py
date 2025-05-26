#1. Contar elementos mayores que 10 
#Dada una lista de números, cuenta cuántos de ellos son mayores que 10. 
numeros = [4,11,7,25,3,17,2]
mayores = []

for numero in numeros:
    if numero > 10:
        mayores.append(numero)
print("De la lista, los numeros mayores que 10 son: ")
for n in mayores:
    print(n)

'''
#otra alternativa con compresion de listas

numeros = [4, 11, 7, 25, 3, 17, 2]
mayores = [n for n in numeros if n > 10]

print("De la lista, los números mayores que 10 son:")
for n in mayores:
    print(n)
'''

#2. Eliminar duplicados de una lista 
#Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los 
#elementos únicos (sin usar set). 

frutas = ["manzana", "pera", "manzana", "naranja", "pera"] 
frutas_unicas = []

for fruta in frutas:
    if fruta not in frutas_unicas:
        frutas_unicas.append(fruta)

print("Elementos unicos: ")

for fruta_unica in frutas_unicas:
    print(fruta_unica)

#3. Invertir una lista manualmente 
#Invierte el orden de una lista sin usar .reverse() ni [::-1]. Usa un bucle. 

numeros = [1, 2, 3, 4, 5] 
numeros_inverso = [None] * len(numeros)
# Tu código aquí 
for indice, valor in enumerate(numeros):
    num_invertido = (-1 * indice) - 1
    numeros_inverso[num_invertido] = valor
print("Invertir la lista manualmente: ")
for i in numeros_inverso:
    print(i)

'''
numeros = [1, 2, 3, 4, 5]
numeros_inverso = [None] * len(numeros)

for i in range(len(numeros)):
    numeros_inverso[len(numeros) - 1 - i] = numeros[i]

print("Invertir la lista manualmente:")
for i in numeros_inverso:
    print(i)

'''
#4. Multiplicar todos los elementos de una lista 
#Dada una lista de números, calcula el producto de todos sus elementos. 

valores = [2, 3, 5, 7] 
rango = len(valores)
multiplicacion = 1

for x in valores:
    multiplicacion *= x

print(f"producto de todos los elementos: {multiplicacion}")


'''
from math import prod
print(f"Producto total: {prod(valores)}")
'''

#5. Filtrar palabras largas 
#Dada una lista de palabras, crea una nueva lista con solo aquellas que tengan más de 5 letras. 
palabras = ["sol", "mariposa", "flor", "programación", "cielo"] 
palabras_filter = []
# Tu código aquí
for palabra in palabras:
    if len(palabra) > 5:
        palabras_filter.append(palabra)

print("Palabras filtradas: ")
for palabra_res in palabras_filter:
    print(palabra_res)


'''
palabras_filter = [p for p in palabras if len(p) > 5]
'''

'''
 Problema de la vida real: Gestión de tareas 
Problema: 
Estás creando una aplicación sencilla de lista de tareas pendientes (to-do list). Necesitas una 
estructura para: 
• Agregar tareas nuevas. 
• Marcar tareas como completadas. 
• Eliminar tareas completadas. 
• Mostrar las tareas pendientes. 
Usa listas para almacenar las tareas. Cada tarea puede representarse como una cadena de 
texto y una lista separada puede usarse para las tareas completadas. 
Sugerencias: 
• tareas = [] 
• completadas = [] 
Este problema te permite practicar: 
• Agregar y eliminar elementos. 
• Recorrer listas. 
• Mover elementos de una lista a otra. 
• Mostrar contenido de forma organizada. 
 
'''

print("---------------------------------")
print("      Mis Tareas Pendientes      ")
print("---------------------------------")

#listas

tareas = []
completadas = []

#funciones 

def agregar_tarea(valor, lista_tarea):
    lista_tarea.append(valor)
    return "Agregado correctamente.\n"

def completar_tarea(posicion, lista_tarea, lista_completadas):
    completado = lista_tarea[posicion]
    del lista_tarea[posicion]
    lista_completadas.append(completado)
    return "La tarea se completo.\n"

def eliminar_tarea(posicion, lista_tarea):
    del lista_tarea[posicion]
    return "La tarea se elimino.\n"

def get_tareas(lista):
    return [f"{indice + 1}. {valor}" for indice, valor in enumerate(lista)]

def contar_tareas(lista):
    pendientes = len(lista)
    return pendientes

#opciones
while True:
    try:
        print("| 1. Agregar Tarea | 2. Completar Tareas | 3. Eliminar Tarea | 4. Ver tareas completadas | 5. Salir")
        x = int(input("Opcion: "))
        if x == 5:
            print("Vuelva pronto :D\n")
            break

        if x == 1:
            print("---------------------------------")
            tareas_recorridas = get_tareas(tareas)
            if tareas_recorridas:
                print("\n".join(tareas_recorridas))
            else:
                print("No hay tareas.")
            print("---------------------------------")
            num_pendientes = contar_tareas(tareas)
            print(f"Tareas pendientes: {num_pendientes}")

            nueva_tarea = input("Tarea por agregar: ")
            mensaje = agregar_tarea(nueva_tarea,tareas)
            print(mensaje)
            
        elif x == 2:
            print("---------------------------------")
            tareas_recorridas = get_tareas(tareas)

            if tareas_recorridas:
                print("\n".join(tareas_recorridas))
            else:
                print("No hay tareas")

            print("---------------------------------")
            num_pendientes = contar_tareas(tareas)
            print(f"Tareas pendientes: {num_pendientes}")

            if len(tareas) < 1:
                print("No hay tareas por completar")
                continue
            tarea_completada = int(input("Numero de tarea por completar: "))

            if tarea_completada < 1 or tarea_completada > len(tareas):
                print("Opcion fuera del rango")
                continue
            
            mensaje = completar_tarea(tarea_completada - 1, tareas, completadas)
            print(mensaje)
                
        elif x == 3:
            print("---------------------------------")
            tareas_recorridas = get_tareas(tareas)
            if tareas_recorridas:
                print("\n".join(tareas_recorridas))
            else:
                print("No hay tareas.")
            print("---------------------------------")
            num_pendientes = contar_tareas(tareas)
            print(f"Tareas pendientes: {num_pendientes}")

            if len(tareas) < 1:
                print("No hay tareas por eliminar")
                continue

            num_tarea_del = int(input("Numero de tarea por eliminar: "))

            if num_tarea_del < 1 or  num_tarea_del > len(tareas):
                print("Opcion fuera del rango.")
                continue
            
            del_tarea = eliminar_tarea(num_tarea_del - 1, tareas)
            print(del_tarea)
               
        elif x == 4:
            print("---------------------------------")
            completadas_recorridas = get_tareas(completadas)
            if completadas_recorridas:
                print("\n".join(completadas_recorridas))
            else:
                print("No hay tareas completadas.")
            print("---------------------------------")
            print(f"Tareas Completadas: {contar_tareas(completadas)}")
            
        else:
            print("Opcion invalida, vuelva a intentarlo")
                

    except ValueError:
        print("Valor invalido.")









  







