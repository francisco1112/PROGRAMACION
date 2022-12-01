"""1.Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
print("Ejercicio 1")
A = int(input("Dime el valor de A: "))
B = int(input("Dime el valor de B: "))
import math
print(math.sqrt((A**2)+(B**2)))

"""2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius."""
print("Ejercicio 2")
Temperatura = int(input("Inserte la temperatura: "))
print((Temperatura - 32)*5/9)
"""3. Calcular la media de tres números pedidos por teclado"""
print("Ejercicio 3")
numero1 = int(input("Un número: "))
numero2 = int(input("Otro número: "))
numero3 = int(input("Otro número: "))

media = (numero1 + numero2 + numero3) /3
print(media)

"""4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra"""
print("Ejercicio 4")
totalcompra = int(input("Total de compra: "))
print(15*totalcompra/100)

"""5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo)."""
print("Ejercicio 5")
numero1 = int(input("Un número: "))
numero2 = int(input("Otro número: "))
total = (numero1 - numero2) 
if total < 0:
    print(total*-1)
elif total >= 0:
    print(total)
    
"""6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos."""
print("Ejercicio 6")
num1 = float(input("Inserte un número: ")) 
num2 = float(input("Inserte otro número: "))
n=abs(num1-num2)
print(n)

"""7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
puede calcular?"""
print("Ejercicio 7")
num = int(input("Introduce un número: "))
import math
print("La raíz cuadrada es: ", math.sqrt(num))
print("La raíz cúbica es: ", math.cbrt(num))

"""8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos)."""
print("Ejercicio 8")
dinero = int(input("Introduce una cantidad: "))
print(dinero)



"""9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:"""
print("Ejercicio 9")
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
if exponente > 0:
    print(base*exponente)
elif exponente == 0:
    print("1")
elif exponente < 0:
    print(1/base*exponente*-1)
    
"""10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:"""
print("Ejercicio 10")
A = int(input("Lado A: "))
B = int(input("Lado B: "))
C = int(input("Lado C: "))

if A != B and A != C and B != C and B != A and C != A and C != B:
    print("Triángulo rectángulo")
elif A == B and A != C and B != C or A == C and A != B and C != B or B == C and C != A and B != A:
    print("Isósceles")
elif A == B and A == C and B == C and C == A and C == B and B == A and B == C:
    print("Equilátero")
else:
    print("Escaleno")
    
"""11. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
por 400."""
print("Ejercicio 11")
año = int(input("Inserte Año: "))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("Año bisiesto")
else:
    print("No es bisiesto")
    
"""12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida."""
print("Ejercicio 12")
tipo = input("Inserte el tipo: ")
tamaño = int(input("Inserte el tamaño: "))
precioinicial = int(input("Inserte el precio: "))
if tipo == "A" and tamaño == 1:
    print(precioinicial + 0.20)
elif tipo == "A" and tamaño == 2:
    print(precioinicial + 0.30)
elif tipo == "B" and tamaño == 1:
    print(precioinicial - 0.30)
elif tipo == "B" and tamaño == 2:
    print(precioinicial - 0.50)
else:
    print("El valor no es correcto")

"""13. El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de
autobuses y lo que debe pagar cada alumno por el viaje."""
print("Ejercicio 13")
alumno = int(input("Inserte los alumnos: "))
if alumno >= 100:
    print(65/alumno)
elif alumno >= 50 and alumno <= 99:
    print(70/alumno)
elif alumno >=30 and alumno <= 49:
    print(95/alumno)
elif alumno < 30:
    print(4000/alumno)
else:
    print("El valor no es correcto")
    
"""14. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada."""
print("Ejercicio 14")
tiempo = int(input("Introduzca el tiempo de llamada: "))
dia = str(input("Introduzca el dia: ")).upper()
turno = str(input("Introduzca el turno: ")).upper()
if tiempo <= 5 and tiempo > 0:
    if dia == "DOMINGO":
        print(3*1/100)
    if dia != "DOMINGO" and turno == "MAÑANA":
        print(15*1/100)
    if dia != "DOMINGO" and turno == "TARDE":
        print(10*1/100)

elif tiempo > 5 and tiempo <= 8:
    if dia == "DOMINGO":
        print(3*1.80/100)
    if dia != "DOMINGO" and turno == "MAÑANA":
        print(15*1.80/100)
    if dia != "DOMINGO" and turno == "TARDE":
        print(10*1.80/100)
    
elif tiempo >= 9 and tiempo <= 10:
    if dia == "DOMINGO":
        print(3*2.50/100)
    if dia != "DOMINGO" and turno == "MAÑANA":
        print(15*2.50/100)
    if dia != "DOMINGO" and turno == "TARDE":
        print(10*2.50/100)

elif tiempo > 10:
    if dia == "DOMINGO":
        print(3*3/100)
    if dia != "DOMINGO" and turno == "MAÑANA":
        print(15*3/100)
    if dia != "DOMINGO" and turno == "TARDE":
        print(10*3/100)
else:
    print("Datos no válidos")
    
"""15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error."""
print("Ejercicio 15")
dia = str(input("Introduce el dia: ")).upper()
if dia == "LUNES":
    print("1")
elif dia == "MARTES":
    print("2")
elif dia == "MIERCOLES":
    print("3")
elif dia == "JUEVES":
    print("4")
elif dia == "VIERNES":
    print("5")
elif dia == "SABADO":
    print("6")
elif dia == "DOMINGO":
    print("7")
else:
    print("Los datos son incorrectos")

"""16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente."""
print("Ejercicio 16")
mes = int(input("Introduce un número: "))
if mes >=1 and mes <= 12:
    if mes == 1:
        print("31")
    if mes == 2:
        print("28")
    if mes == 3:
        print("31")
    if mes == 4:
        print("30")
    if mes == 5:
        print("31")
    if mes == 6:
        print("30")
    if mes == 7:
        print("31")
    if mes == 8:
        print("31")
    if mes == 9:
        print("30")
    if mes == 10:
        print("31")
    if mes == 11:
        print("30")
    if mes == 12:
        print("31")
else:
    print("Los datos son incorrectos")






"""8.
2€ = 3
1€ = 4
0.50€ = 2
0.20€ = 5
0.10€ = 6
0.05€ = 3
0.02€ = 5
0.01€ = 15
Tiene que aparecer por pantalla los euros y los centimos.
Si queremos que nos muestre los centimos,si por ejemplo tenemos 105,53€, al restarlo por los euros solamente, en esta caso seria restarlo con 105€, nos daría los céntimos.
"""



"""Investigar el TRUNC y el ROOM"""
"""tenemos 15 min, 
5 min * 1€
3 min * 0.8€
2 min * 0.7€
5 min * 0.5€"""

