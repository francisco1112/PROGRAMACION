'''
Created on 13 oct 2022

@author: Paco
'''
'''1. Realizar un programa que lea un número entero por teclado e informe de si
el número es par o impar (el cero se considera par).'''
numero= int(input("Pon un número: "))
if numero % 2 == 0:
    print("Es número par")
else:
    print("Es número impar")
    
'''2. Realizar un programa que solicite dos números por teclado e imprima en
pantalla si son iguales, el primero mayor que el segundo o el primero más
pequeño que el segundo.'''
numero1 = int(input("Dime un número: ")) 
numero2 = int(input("Dime otro número: ")) 
if numero1 > numero2:
    print("numero1 > numero2")  
elif numero1 < numero2:
    print("numero2 > numero1")
else:
    print("numero1 = numero2")
    
'''3. Realizar un programa que lea un número por teclado. El programa debe
imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
el programa finaliza sin mostrar ningún mensaje.'''
    
numero = int(input("Un número: "))
if numero % 2 == 0:
    print("Es múltiplo de 2")  
elif numero % 3 == 0:
    print ("Es múltiplo de 3")
elif numero % 2 == 0 and numero % 3 == 0:
    print("Es múltiplo de 2 y 3")
else:
    print("No es múltiplo ni de 2, ni de 3")
    
''' 4. Realizar un programa que lea la edad de una persona menor a 100 años e
informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
29) o un adulto.'''  
    
edad = int(input("Dime tu edad: ")) 
if edad>=0 and edad<=12:
    print("Niño")  
elif edad>=13 and edad<=17:
    print("Adolescente")
elif edad>=18 and edad<=29:
    print("Joven")
elif edad>=30 and edad<=100:
    print("Adulto")
else:
    print("La edad no está en el rango")
    
'''5. Realizar un programa que solicite 4 números e imprima la media de los
números. También debe imprimir aquellos números que son superiores a la
media.'''
numero1 = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))
numero3 = int(input("Tercer numero: "))
numero4 = int(input("Cuarto numero: "))

media = (numero1 + numero2 + numero3 + numero4) /4

if numero1 > media:
    print("El número %s es mayor a la media %s de los números" % (numero1, media))
if numero2 > media:
    print("El número %s es mayor a la media %s de los números" % (numero2, media))
if numero3 > media:
    print("El número %s es mayor a la media %s de los números" % (numero3, media))
if numero4 > media:
    print("El números %s es mayor a la media %s de los números" % (numero4, media))


"""6. Realizar un programa que solicite un carácter por teclado e informe por
pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc."""

vocala=input("Dime una vocal: ").upper()

if vocala=="A":
    print("Es la primera vocal (A)")
elif vocala == "E" or vocala == "I" or vocala == "O" or vocala == "U":
    print("Es vocal")
else:
    print("No es vocal")
    
vocalb=input("Dime una vocal: ").upper()

if vocalb=="E":
    print("Es la segunda vocal (E)") 
elif vocalb == "A" or vocalb == "I" or vocalb == "O" or vocalb == "U":
    print("Es vocal")
else:
    print("No es vocal")
    
vocalc=input("Dime una vocal: ").upper()

if vocalc=="I":
    print("Es la tercera vocal (I)")
elif vocalc == "E" or vocalc == "A" or vocalc == "O" or vocalc == "U":
    print("Es vocal")
else:
    print("No es vocal")
    
vocald=input("Dime una vocal: ").upper()

if vocald=="O":
    print("Es la cuarta vocal (O)")
elif vocald == "E" or vocald == "I" or vocald == "A" or vocald == "U":
    print("Es vocal")
else:
    print("No es vocal")
    
vocale=input("Dime una vocal: ").upper()

if vocale=="U":
    print("Es la quinta vocal (U)")
elif vocale == "E" or vocale == "I" or vocale == "O" or vocale == "A":
    print("Es vocal")
else:
    print("No es vocal")

#HE PROBADO ESTE, PERO NO ESTA BIEN.
"""vocal=input("Dime una vocal: ").upper()

if vocal=="A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U":
    print(f"Es la vocal {vocal}")
elif vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U" or vocal == "A":
    print("Es vocal")
else:
    print("No es vocal")"""
    
    
    
"""7. Realizar un programa que lea el estado civil de una persona (S-Soltero, C-
Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
siguientes reglas:"""
estadocivil=input("estadocivil: ")
años=int(input("años: "))
precio=int(input("precio: "))
if estadocivil == "S":
    print(12*precio/100)
elif estadocivil == "D" and años < 35:
    print(12*precio/100)
elif años > 50:
    print(8.5*precio/100)
elif estadocivil == "V" or estadocivil == "C" and años < 35:
    print(11.3*precio/100)
else:
    print(10.5*precio/100)
    
"""8. Realizar un programa que lea por teclado dos marcaciones de un reloj
digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
23:59:59 e informe cual de ellas es mayor."""
hora1, min1, seg1 = 0, 12, 59
hora2, min2, seg2 = 0, 20, 20
if hora1 < hora2:
    print("la hora 1 es menor que la hora 2")
elif hora2 < hora1:
    print("la hora 2 es menor que la hora 1")
else:
    if min1 < min2:
        print("la hora 1 es menor que la hora 2")
    elif min1 > min2:
        print("la hora 2 es menor que la hora 1")
    else:
        if seg1 < seg2:
            print("la hora 1 es menor que la hora 2")
        elif seg1 > seg2:
            print("la hora 2 es menor que la hora 1")
        else:
            print("Las horas coinciden")
   



"""9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
porcentaje de rebaja que se aplicará sobre el precio original del producto se
calcula de la siguiente forma:"""

producto=input("producto: ")
precio=int(input("precio: "))
if producto == "A":
    print(7*precio/100)
elif producto == "C" or precio < 500: 
    print(12*precio/100)
else:
    print(9*precio/100)
    
    
"""10.Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error"""

caracter = str(input("Un carácter: "))
numero1 = int(input("Un número: "))  
numero2 = int(input("Otro número: "))

if caracter == "*":  
    print(numero1+numero2)
elif caracter == "/":
    print(numero1+numero2)
elif caracter == "+":
    print(numero1+numero2)
elif caracter == "-":
    print(numero1+numero2)
else:
    print("No es válido")


    






"""numero = 81
exponente = 2
print(numero**(1/exponente)) #raiz cuadrada
print(math.sqrt(numero))#raiz cuadrada
print(numero**exponente) #potencia
print(math.pow(numero, exponente)"""


"""numero = 81
print(numero**(1/2)) #raiz cuadrada
print(math.sqrt(numero))#raiz cuadrada
print(numero**2) #potencia
print(math.pow(numero, 2)"""


"""range(inicio, fin, incremento)
for variable in range(10):
    print(variable)"""
    