

#EJERCICIO1
print("El número menor de la lista")

from random import randint

lista=[]

for i in range (100):
    lista.append(randint(0, 500))
print(lista)

def obtenerElementoMenor(lista):
    
    menor = lista [0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor=lista[i]
    
    return menor
print(obtenerElementoMenor(lista))

print("El número mayor de la lista")



lista1=[]

for i in range (100):
    lista1.append(randint(0, 500))
print(lista1)

def obtenerElementoMayor(lista1):
    
    mayor = lista1 [0]
    for i in range(len(lista1)):
        if lista1[i] > mayor:
            mayor=lista1[i]
    
    return mayor
print(obtenerElementoMayor(lista1))

print("Obtiene la suma de todos los números")

from random import randint

def obtenerSuma(lista):
    suma = 0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma
print(lista)
def genera_lista_numeros_aleatorios(size=100):
    lista_aleatorios = []
    for i in range(size):
        lista_aleatorios.append(randint(0,100))
    return lista_aleatorios


listaNumeros = genera_lista_numeros_aleatorios(5)



print(obtenerSuma(listaNumeros))

print("-------------------------------------")

lista2=[]

for i in range (5):
    lista2.append(randint(0, 5))
print(lista2)

def obtenerSuma(lista2):
    
    suma = lista2 [0]
    for i in range(len(lista2)):
            suma+=lista2[i]
    
    return suma
print(obtenerSuma(lista2))

print("Obtiene la media de todos los números")

lista3=[]

for i in range (2):
    lista3.append(randint(0, 5))
print(lista3)

def obtenerMedia(lista3):
    
    media = lista3 [0]
    for i in range(len(lista3)):
            media+=lista3[i]
            
    return media/i
print(obtenerMedia(lista3))





def es_par(numero):
    return numero % 2 == 0
def es_impar(numero):
    return not es_par(numero)




def factorial(numero):
    total =1
    for i in range(numero):
        total*=i+1
    return total
print factorial(7)




#EJERCICIO 2
def desplazar(lista):
    a_escribir = lista[0]
    a_guardar = 0
    
    for i in range(len(lista)):
        if i == len(lista)-1:
            lista[0]=a_escribir
        else:
            a_guardar = lista[(i+1)]
            lista[(i+1)]=a_escribir
            a_escribir=a_guardar
            
    return (lista)

lista_numeros = [1, 3, 5, 7]
print(desplazar(lista_numeros))


#EJERCICIO 3
day = int(input("DIA: "))
month = int(input("MES: "))
year = int(input("YEAR: ")) 

def es_bisiesto(year):
    bisiesto = year%4==0 and (year%100!=0 or year%400==0)
    return (bisiesto)

def es_fecha_valida(day, month, year):
    dias_max_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    fecha_valida = 1<=month<=12 and ((1<=day<=dias_max_por_mes[month-1]) or (es_bisiesto(year) and 1<=day<=29 and month==2))
    return fecha_valida

def transformar_formato_largo(day, month, year):
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    if es_fecha_valida(day, month, year):
        
        mensaje = f"{day} de {meses[month-1]} de {year}"
        
    else:
        mensaje = "La fecha introducida no es válida."
    
    return (mensaje)
print(transformar_formato_largo(day, month, year))

#EJERCICIO 4
#numero = int(input("Introduce un numero: "))
lista_numbers= []
while numero >= 0:
    lista_numbers.append=numero
    #numero = int(input("Introduce nuevo numero: "))
while numero < 0:
    def es_par(numero):   
        return numero % 2 == 0
       
    print(es_par(numero))
    def obtenerElementoMayor(lista_numbers):   
    mayor = numero [0]
    for i in range(len(lista_numbers)):
        if lista_numbers[i] > mayor:
            mayor=lista_numbers[i]
        
    return mayor
    print(obtenerElementoMayor(lista_numbers))




#EJERCICIO 5
lista = ["Di", "buen", "dia", "a", "papa"]

invertida=[]
def poner_inversa(lista):
    invertida=[]
    for i in lista:
        invertida=[i]+invertida
    return (invertida)

print(poner_inversa(lista))


#EJERCICIO 6

lista_elementos = [1,2,2,4]
def estaOrdenada(lista_elementos):
    ordenada = True
    for i in range(len(lista_elementos)-1):   
        if lista_elementos[i]>lista_elementos[i+1]:
        
            ordenada = False
    
    return ordenada
print(estaOrdenada(lista_elementos))



#EJERCICIO 7
listaA =[1,3]
listaB = [2,3]
def encajan(listaA, listaB):
    encajan = "No encajan"
    
    if ((listaA[0] or listaA[1]) == listaB[0]) or ((listaA[0] or listaA[1]) == listaB[1]) or ((listaB[0] or listaB[1]) == listaA[0]) or ((listaB[0] or listaB[1]) == listaA[1]) or (listaA[1]==listaB[1]) :
        encajan = "Encajan"
        
    return encajan

print(encajan(listaA, listaB))
    




#EJERCICIO 8
n = 10000000000000000
#a)
def es_numero_primo(n):
    es_primo = True
    
    for i in range(2,n):
        if n%i==0:
            es_primo = False 
    
    return es_primo

lista = [1,4,5,6,7,8894,12,54657,34,2,31,17]
primos = []
for elemento in lista:
    if es_numero_primo(elemento):
        primos.append(elemento)
        
print(primos)


#b)

def obtenerSuma(primos):
    suma = 0
    for i in range(len(primos)):
        suma+=primos[i]
    return suma

print(obtenerSuma(primos))

#c)

def obtenerMedia(primos):
    
    media = 0
    for i in range(len(primos)):
            media+=primos[i]
            
    return media/i
print(obtenerMedia(primos))

#d)
lista_factoriales=[]
def sacar_factorial(primos):
    for elemento in primos:
        lista_factoriales.append(math.factorial(elemento))
        
def factorial (n):
    resultado = 1
    for i in range(1, n+1):
        resultado*=i 
    return resultado
print("Factorial de la posicion 0 de la lista de numeros primos: ")
print(factorial(primos[0]))
print("Factorial de la posicion 1 de la lista de numeros primos: ")
print(factorial(primos[1]))
print("Factorial de la posicion 2 de la lista de numeros primos: ")
print(factorial(primos[2]))
print("Factorial de la posicion 3 de la lista de numeros primos: ")
print(factorial(primos[3]))
print("Factorial de la posicion 4 de la lista de numeros primos: ")
print(factorial(primos[4]))
print("Factorial de la posicion 5 de la lista de numeros primos: ")
print(factorial(primos[5]))
        


#EJERCICIO 9
lista1=[44,36,32,11,113,56,77]
n=45


def obtenerMayores(lista1, n):
    numeros_mayores=[]
    for i in lista1:
        if i > n:
            numeros_mayores.append(i)
    
    return numeros_mayores
    
print(obtenerMayores(lista1, n))  

def obtenerMenores(lista1, n):
    numeros_menores=[]
    for i in lista1:
        if i < n:
            numeros_menores.append(i)
    
    return numeros_menores

print(obtenerMenores(lista1, n))

def obtenerMultiplo(lista1, n):
    multiplo=[]
    for i in lista1:
        if i % n == 0:
            multiplo.append(i)
            
    return multiplo

print(obtenerMultiplo(lista1, n))


#EJERCICIO10
n=input("introduce un numero Decimal: ").lower()
def convierteBinario_a_Decimal(numero):
    decimal=[]
    sumadecimal=0
    if numero[-1]=="b":
        numero=numero[0:-1]
        for i in range(len(numero)):
            valor=(2**i)*(int(numero[i]))
            decimal.append(valor)
            sumadecimal+=valor
    return decimal, sumadecimal
print(convierteBinario_a_Decimal(n))

#EJERCICIO11

#EJERCICIO12

#EJERCICIO13

listaNombres=["Marta", "Andres", "Angela", "Pedro", "Maria"]
letra=input("Introduce una letra: ").upper()
def comprobarNombres(lista, l):
    listaNombres1=[]
    for i in range(len(lista)):
        if l==lista[i][0]:
            listaNombres1.append(lista[i])
    return listaNombres1
    
print(comprobarNombres(listaNombres, letra))

#EJERCICIO14


