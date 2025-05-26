print("---------------------------------")
print("      Mis Tareas Pendientes      ")
print("---------------------------------")

# listas
tareas = []
completadas = []

# funciones 
def agregar_tarea(valor, lista_tarea):
    lista_tarea.append(valor)
    return "Agregado correctamente.\n"

def completar_tarea(posicion, lista_tarea, lista_completadas):
    completado = lista_tarea[posicion]
    del lista_tarea[posicion]
    lista_completadas.append(completado)
    return "La tarea se completó.\n"

def eliminar_tarea(posicion, lista_tarea):
    del lista_tarea[posicion]
    return "La tarea se eliminó.\n"

def get_tareas(lista):
    return [f"{indice + 1}. {valor}" for indice, valor in enumerate(lista)]

def contar_tareas(lista):
    return len(lista)

# menú de opciones
while True:
    try:
        print("| 1. Agregar Tarea | 2. Completar Tareas | 3. Eliminar Tarea | 4. Ver tareas completadas | 5. Salir")
        x = int(input("Opción: "))
        
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
            print(f"Tareas pendientes: {contar_tareas(tareas)}")

            nueva_tarea = input("Tarea por agregar: ")
            mensaje = agregar_tarea(nueva_tarea, tareas)
            print(mensaje)

        elif x == 2:
            print("---------------------------------")
            tareas_recorridas = get_tareas(tareas)
            if tareas_recorridas:
                print("\n".join(tareas_recorridas))
            else:
                print("No hay tareas.")
            print("---------------------------------")
            print(f"Tareas pendientes: {contar_tareas(tareas)}")

            if len(tareas) < 1:
                print("No hay tareas por completar.")
                continue
            tarea_completada = int(input("Número de tarea por completar: "))
            if tarea_completada < 1 or tarea_completada > len(tareas):
                print("Opción fuera del rango.")
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
            print(f"Tareas pendientes: {contar_tareas(tareas)}")

            if len(tareas) < 1:
                print("No hay tareas por eliminar.")
                continue
            num_tarea_del = int(input("Número de tarea por eliminar: "))
            if num_tarea_del < 1 or num_tarea_del > len(tareas):
                print("Opción fuera del rango.")
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
            print("Opción inválida, vuelva a intentarlo.")

    except ValueError:
        print("Valor inválido.")
