#1. pedir dos numeros al usuario e imprime su suma

valor1 = int(input("Ingrese el primer numero: "))
valor2 = int(input("Ingrese el segundo numero: "))
suma = valor1 + valor2
print(suma)

print("-----------------------")

#2. Pide un número e imprime si es par o impar
valor1 = float(input("Ingrese un numero: "))

if valor1 % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero es impar")

print("-----------------------")

#3. Pide la base y la altura de un triangulo y muestra su área

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
undMedida = input("Unidad de medida: ")

areaTriangulo = base * altura / 2

print("El area del triangulo es: ",areaTriangulo," "+undMedida+ "²")

#4. Pide dos números y una operacion (+,-,*,/) y realiza el cálculo.
print("--Calculadora---")
var1 = float(input("Ingrese el primer valor: "))
var2 = float(input("Ingrese el segundo valor: "))

suma = var1 + var2
resta = var1 - var2
multiplicacion = var1 * var2

if(var2 == 0):
    division = "No se puede dividir entre 0"
else:
    division = var1 / var2

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("Division: ", division)

#5. imprime los números del 1 al 10 usando un bucle for

for i in range (1,11):
    print(i)

#6. Pide un número e imprime su tabla de multiplicar del 1 al 10

for i in range (1,11):
    print("------- tabla del ", i, "-------")
    for x in range (1,13):
        res = i * x
        print(i," * ",x," = ",res)

print("---------------------------------------")

#7. Pide un número N y suma todos los números desde 1 hasta N.
#  
N = int(input("Introduce un número: "))
suma = 0

for i in range(1, N + 1):
    suma += i

print(f"La suma de los números del 1 al {N} es {suma}")



print("---------------------------------------")

#8. Pide tres números al usuario e imprime cuál es el mayor

print("Ingrese el primer numero: ")
var1 = int(input())
print("Ingrese el segundo numero: ")
var2 = int(input())
print("Ingrese el tercer numero: ")
var3 = int(input())
print("Resultado: ")
if(var1 > var2 and var1 > var3):
    print(var1, " es el mayor")
elif(var2 > var1 and var2 > var3):
    print(var2, " es el mayor")
else:
    print(var3, " es el mayor")

print("-------------------------------")


#9 pide una temperatura en grados Celsius y conviértela a Fahrenheit
celsius = float(input("Ingrese una temperatura en grados celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("Grados Fahrenheit: ", fahrenheit)


print("-------------------------------")


#10 Pide un número y di es primo o no
var1 = int(input("Ingrese un numero: "))
esPrimo = True

if var1 < 2:
    es_primo = False
else:
    for i in range(2, int(var1 ** 0.5) +1):
        if var1 % i == 0:
            esPrimo = False
            break

if esPrimo:
    print(f"{var1} es primo.")
else:
    print(f"{var1} no es primo.")
            
    