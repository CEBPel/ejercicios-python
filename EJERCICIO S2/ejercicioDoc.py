#1.Escribir una función que reciba un nombre y edad, y devuelve un saludo personalizado

def saludo(nombre, edad):
    if edad < 18:
        return f"Hola {nombre}, niño skibidi, yo le se a los brainrot (Capuccina y tralalerotralala :D xd?) "
    else:
        return f"{nombre}, bienvenido a: ¡Abandone la esperanza, todo aque que entre aqui!, preparaos😈"

mensaje = saludo("rafael", 19)
print(mensaje)

#2. Crear una función que reciba 3 números y devuelva el mayor.
def calcular_mayor(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
mayor = calcular_mayor(4,7,8)    
print(f"El mayor es: {mayor}")

#3. Hacer una función que calcule el factorial de un número.

def calcular_factorial_w(a):
    contador = 1
    factorial = 1

    while contador <= a:
        factorial *= contador
        contador += 1
    return factorial
    

factorial_resultado = calcular_factorial_w(5)
print(f"El factorial de 5! es: {factorial_resultado}")

def calcular_factorial_f(a):
    factorial = 1
    for i in range(1, a + 1):
        factorial *= i
    return factorial

factorial_resultado = calcular_factorial_f(4)
print(f"El factorial de 4! es: {factorial_resultado}")


#4. Escribir una función que diga si un número es primo

def identificar_numeros_primos(valor):
    esPrimo = True

    if valor < 2:
        esPrimo = False
    else:
        for i in range(2, int(valor ** 0.5) + 1):
            if valor % i == 0:
                esPrimo = False
                break
    if esPrimo:
        return f"{valor} es primo"
    else:
        return f"{valor} no es primo"

respuesta = identificar_numeros_primos(29)
print(respuesta)




