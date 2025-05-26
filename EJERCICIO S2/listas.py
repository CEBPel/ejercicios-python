#crear lista
mi_lista = [1,2,3,4,5]
mi_lista2 = ["manzana","banana","pera"]
mi_lista3 = [1,"hola",True,3.14]

#acceder a elementos
mi_lista = [10,20,30,40]
print(mi_lista[0]) # 10 (primer elemento)
print(mi_lista[-1]) # 49 (último elemento)

#recorrer una lista
for elemento in mi_lista:
    print("r: ", elemento)

#modificar elementos
mi_lista.append(60) # agrega al final
mi_lista.insert(2,25) # inserta en indice 2
mi_lista.extend([70,80]) #agrega varios elementos
print(mi_lista)

#eliminar elementos
mi_lista.remove(30) #elimina el primer 30 que encuentre
mi_lista.pop() # elimina el ultimo
mi_lista.pop(1) # eliminael elemento en indice 0
del mi_lista[0] # elimina el elemento en indice 0
mi_lista.clear() # vacia la lista

#operaciones útiles
len(mi_lista) # largo de la lista
mi_lista.sort() # ordena la lista (si son del mismo tipo)
mi_lista.reverse() # invierte la lista

#verficar si un elemento está en la lista:
mi_lista = [10,20,30,40]
if 10 in mi_lista:
    print("10 está en la lista")

# slicing (sublistas)
sublista = mi_lista[1:4] # Elementos del indice 1 al 3
print(sublista)

#compresión de listas (List Comprehension)
cuadrados = [x**2 for x in range(5)]

print(cuadrados)

