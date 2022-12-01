print("------BOLETIN6------")
"""1. Diseñe un programa para mostrar todos los números entre 1 y 100. Si el número es un
múltiplo de 7, debe mostrar el mensaje "El número xx es un múltiplo de 7". Si el
número es un múltiplo de 13, debe mostrar el mensaje "El número xx es un
múltiplo de 13". Si el número es un múltiplo de 7 y 13, debe mostrar ambos
mensajes"""
numero = int(input("Inserte un número: "))
while numero <= 0 or numero > 100:
    numero = int(input("Inserte un número del 1 al 100 por favor: "))
if numero %7 == 0:
    print(f"El número {numero} es un múltiplo de 7")
elif numero %13 == 0:
    print(f"El número {numero} es un múltiplo de 13")
elif numero %7 == 0 and numero %13 == 0:
    print(f"El numero {numero} es múltiplo de 7 y de 13")
else:
    print(f"El numero {numero} no es múltiplo de 7 ni de 13")    
    
"""2. Diseña un programa para leer un número entero entre 0 y 10 y muestra la tabla de multiplicar.
Para solicitar el número debe mostrar el siguiente mensaje "Ingrese un número
entre 0 y 10”. Si el número está fuera de los límites, el programa debería mostrar
el mensaje "El número está fuera de los límites". Si el número es válido, debe
mostrar la tabla de tiempos siguiendo el siguiente formato:"""
numero = int(input("Inserte un número: "))
while numero < 0 or numero > 10:
    numero = int(input("Inserte un número del 0 al 10 por favor: "))
for i in range(0,11):
    print(f'{numero} * {i} = {numero * i}')

"""3. Diseña un programa que pregunte cuántos números quiere introducir el usuario. Después,
el usuario tendría que introducir los números uno a uno y el programa debería
decir si cada uno de los números es par o impar. Si el usuario ingresa 0 o un negativo
número, no es válido, y el sistema debe pedir otro número. Los mensajes
son los siguientes:
"¿Cuántos números desea ingresar?" para pedir la cantidad de números.
“Ingrese un número mayor que 0:” para solicitar un número.
“El número no es válido, debe ser mayor a 0” para informar que el número no es
válido.
“El número XX es impar”
“El número XX es par”
"""
cantidad = int(input("¿Cuántos números desea introducir? "))
while cantidad <= 0:
    cantidad = int(input("El número no es válido, debe ser mayor a 0: "))
while cantidad > 0:
    numero = int(input("Introduce número: "))
    while numero <= 0:
        numero = int(input("El número no es válido, debe ser superior a 0: "))
    if numero%2 == 0:
        print(f"El número {numero} es par")
    elif numero%1 == 0:
        print(f"El número {numero} es impar")
    cantidad-=1
"""4. Diseña un programa que lea un número positivo N mayor que 0 y muestre el resultado
de la suma de los N números entre 1 y N. Si el número N no es válido, el
el programa debería pedirlo de nuevo. Los mensajes son los siguientes:
“Ingrese un número mayor que 0:”
“El número no es correcto, inténtalo de nuevo.”
“La suma de los N primeros números es XX.”"""
cantidad = int(input("¿cuántos números sumamos? "))
total = 0
contador = 0
while cantidad > contador:
    numero = int(input("Introduce un numero: "))
    total+=numero
    contador+=1
print(f"La suma de los {cantidad} primeros números es {total}.")

"""5. Diseñe un programa que solicite números hasta que el usuario ingrese uno negativo. Cuando
esto sucede, el programa mostrará cuántos números positivos han sido
introducido por el usuario. Los mensajes son los siguientes:
“Ingrese un número (negativo para terminar):”
"Ha ingresado XX números positivos"."""
numero = int(input("Introduce un número: "))    
total = 0
while numero > 0:
    numero = int(input("Introduce otro número: "))
    total+=1
print(f"Ha ingresado {total} números positivos")

"""6. Diseñe un programa que lea dos números enteros, por ejemplo númeroA y
númeroB, y calcula el producto de ambos números sin usar la multiplicación, pero
utilizando la suma. Los mensajes son los siguientes:
“Ingrese un número:”
“El producto es XX”"""
numeroA = int(input("Introduce un número: "))
numeroB = int(input("Introduce otro número: "))
producto = 0
while numeroB != 0:
    producto+=numeroA
    numeroB-=1
print(f"“El producto es {producto}”")
    
"""7. Diseña un programa que pregunte cuántos números quiere escribir el usuario. Después de la
usuario ingresa todos los números, el programa debe decir el medio de los números. Si el
el usuario ingresa un número incorrecto, el programa debería solicitarlo nuevamente. los mensajes son
el seguimiento:
"¿Cuántos números desea ingresar?" para pedir la cantidad de números.
“Ingrese un número mayor que 0:” para solicitar un número.
“El número no es válido, debe ser mayor a 0” para informar que el número no es
válido.
“El medio es XX.XX” para mostrar el resultado."""
cantidad = int(input("¿Cuántos números desea ingresar? "))

while cantidad <= 0:
    cantidad = int(input("¿Cuántos números desea ingresar? "))
total= 0
contador = 0

while cantidad > contador:
    numero = int(input("Ingrese un número mayor que 0: "))
    while numero <= 0:
        numero = int(input("El número no es válido, debe ser mayor a 0"))
    contador +=1
    total += numero
print(f"La media es {total/cantidad}")

"""8. Diseñe un programa que solicite un conjunto de números. Después de ingresar cada número, el
El programa debe preguntar "¿Desea ingresar más números (S/N)?". Si la respuesta es "S"
el programa pide otros números. Cuando el usuario termine de ingresar todos los números,
el programa debe decir cuál es el más pequeño. Los mensajes son los siguientes:
“Ingrese un número:”
“¿Quieres ingresar más números (S/N)?”
“El número más pequeño es XX”"""
numero = int(input("Ingrese un número: "))
peque = numero
pregunta = input("¿Desea ingresar más números (S/N)? ")
while pregunta.upper()=="S":
    numero = int(input("Ingrese otro número: "))
    if numero < peque:
        peque = numero
    pregunta = input("¿Desea ingresar más números (S/N)? ")
print(f"El número menor es {peque}")

"""9. Diseñe un programa que lea un número entero positivo mayor que 0 y diga si
es un "número perfecto". Un número es perfecto si es igual a la suma de todos sus divisores.
Los mensajes son los siguientes:
“Ingrese un número entero positivo mayor que 0:”
“El número no es válido, inténtalo de nuevo.”
“El número es perfecto”.
“El número no es perfecto”."""  
numero = int(input("Ingrese un número entero positivo mayor que 0:"))
while numero < 1:
    numero = int(input("El número no es válido, inténtalo de nuevo."))

sumaDivisores = 0

for i in range(1, numero):
    if numero%i==0:
        sumaDivisores+=i
        
if sumaDivisores == numero:
    print("El número es perfecto.")
else:
    print("El número no es perfecto.")
    
print("-------------------------------") 
    
numero = int(input("Ingrese un número entero positivo mayor que 0:"))
while numero < 1:
    numero = int(input("El número no es válido, inténtalo de nuevo."))
contador = 1
sumaDivisores = 0

while contador < numero:
    if sumaDivisores == numero:
        print("El número es perfecto.")
    else:
        print("El número no es perfecto.")
    numero-=1
"""10. Diseñe un programa que lea un número entero positivo y diga el “factorial” de
el número. Para calcular el factorial debes saber que
HECHO(0)= 1
HECHO(1) =1
HECHO(N)= N*(N-1)*(N-2)*....1
Los mensajes son los siguientes:
“Ingrese un número entero positivo:”
“El número no es válido, inténtalo de nuevo.”
“El factorial es XX”"""
total = 1 
numero = int(input("Ingrese un número: "))
while numero < 0:
    numero = int(input("El número no es válido, inténtalo de nuevo: "))
for i in range(1, numero+1):
    total *=i
   
print(f"El factorial es: {i}")

print("------BOLETIN4------")
        
"""17. Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario"""
num1 = int(input("Inserte un numero: "))
num2 = int(input("Inserte otro numero: "))
for i in range(num1,num2,2):
    print(i)
    
"""18. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo."""
inferior = int(input("Límite inferior: "))
superior = int(input("Límite superior: "))
while inferior >= superior:
    inferior = int(input("El límite superior tiene que ser mayor al inferior: "))
    numero = int(input(f"Introduzca un número entre {inferior} y {superior}: "))

suma = 0
fuera = 0
igual = 0
while numero != 0:
    
    if inferior < numero < superior:
        suma+=numero
    elif numero < inferior or numero > superior:
        fuera+=1
    else:
        igual+=1
    numero = int(input(f"Introduzca un número entre {inferior} y {superior}: "))
        
print(f"La suma de los numeros dentro del intervalo es {suma}, fuera del intervalo hay {fuera} numeros")
print(f"Existe {igual} numeros iguales al intervalo")


"""19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
de potencia."""
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

potencia = 1
for i in range(exponente):
    potencia *=base
print("La potencia es:", potencia)

"""20. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses."""

pago = 10   
suma = pago

print(f"El pago del mes 1 es {pago}")
for i in range (2, 21):
   
    pago*=2
    print(f"El pago del mes {i} es {pago}")
    suma+=pago
       
print(f"El total es {suma}€") 
    


        