"""
Programación Modular II:
#EJERCICIO1
1. Diseñe un método llamado computaFactorial que reciba un entero positivo y
devuelve el factorial para ese número. Si el número es negativo, el método debe
devuelve Ninguno.
"""
n = int(input("Introduce un numero positivo: "))

if n < 0:
    print(None)
    
if n>=0:   
    def computeFactorial (n):
        resultado = 1
        
        for i in range(1, n+1):
            resultado*=i
            
        return resultado
    
    print(computeFactorial(n))
    

"""
#EJERCICIO2
2. Diseñe un método llamado esAñoBisiesto que reciba un número y devuelva Falso para
años comunes y True para años bisiestos. Usted puede saber que un año se considera
ser un año bisiesto si es divisible por 4, a menos que también sea divisible por 100. Un año no es un
año bisiesto si es divisible por 100 a menos que también sea divisible por 400

"""
year = int(input("Introduce un año para saber si es bisiesto: "))

def esAnioBisiesto(year):
    bisiesto = False
    
    if year%4==0 and (year%100!=0 or year%400==0):
        bisiesto = True
        
    return (bisiesto)

print(esAnioBisiesto(year))

"""
#EJERCICIO3
3. Diseñe un método llamado computeDaysInMonth que devuelva el número de días para
el mes y el año que se reciben como argumentos. Puede utilizar el método
año bisiesto anterior. Si los valores no son válidos, el método debería devolver -1
"""
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
        mensaje = "-1"
    
    return (mensaje)

print(transformar_formato_largo(day, month, year))

"""
#EJERCICIO4
4. Diseñe un método llamado getDayOfWeek que reciba una lista que contenga tres números enteros
(día, mes y año) y devuelve el día de la semana para esa fecha (lunes,
Martes Miércoles Jueves Viernes Sábado Domingo).
Puede usar el siguiente algoritmo para obtener un número entre 0 (domingo) y 6
(sábado) correspondiente al día de la semana para una fecha dada:
"""
a = (14 - month) / 12
y = year – a
m = month + 12 * a – 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7

def getDayOfWeek(day, month, year):
    a=(14-month)//12
    
    y=year-a
    
    m=month+12*a-2
    
    return(int(day+y+y//4-y//100+y//400+(31*m)//12)%7)

nameOfDays=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day=1
while day>0:
    day=int(input("Enter a number of day: "))
    month=int(input("Enter a number of month: "))
    year=int(input("Enter a number of year: "))
    if day>0:
        text=nameOfDays[getDayOfWeek(day, month, year)]
        
    else:
        text: "ERROR!"
        
    print("\n",text,"\n")

"""
#EJERCICIO5
5. Diseñe un método llamado powerIt que reciba dos enteros y eleve el primero
número al segundo. Puede usar el producto o la recursividad y verificar los valores. Si
no se proporciona ningún exponente, el primer número se eleva a 0.
"""
numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce otro numero: "))
def powerlt (numero1, numero2):
    if numero2 == 0:
        elevar=numero2**0
    else: 
        elevar=numero2**numero1
    return elevar
print(powerlt(numero1, numero2))

"""
#EJERCICIO6
6. Diseñe un método llamado getNumberOfDigits que reciba un número (puede ser
real, entero, positivo o negativo) y debe devolver el número de dígitos que contiene. Si
el parámetro no es válido, el método debería devolver Ninguno. Extender esta función a
otros sistemas numéricos (hexadecimal, decimal, binario, octal).
"""
def getNumberOfDigitsDecimal(number):
    count=0     
    listdot=" "
    listothers=""
    for i in range(len(number)):
        if(number[i]=="."):
            listdot+=number[i]
            
        if not(number[i]=="0" or number[i]=="1" or number[i]=="2" or number[i]=="3" or number[i]=="4" or number[i]=="5" or number[i]=="6" or number[i]=="7" or number[i]=="8" or number[i]=="9" or number[i]=="." or number[i]=="-"):
            listothers+=number[i]
        
        if(len(listothers)>0)or("-"in number[1:-1])or("-"in number[-1])or("." in (number[0] or number[-1]))or(".." in number)or(".." in listdot)or ("-." in number):
            count=None
        elif ("0" in number[i]) or ("1"in number[i]) or ("2"in number[i]) or ("3"in number[i]) or ("4"in number[i]) or ("5"in number[i]) or ("6"in number[i]) or ("7"in number[i]) or ("8"in number[i]) or("9"in number[i]): 
            count+=1
    
    return count

def getNumberOfDigitsBinary(number):
    count=0     
    listdot=" "
    list0_1=""
    for i in range(len(number)):
        if(number[i]=="."):
            listdot+=number[i] 
        if not(number[i]=="1" or number[i]=="0" or number[i]=="-" or number[i]=="."):
            list0_1+=number[i]   
        if("-." in number)or(len(list0_1)>0)or("-"in number[1:-1])or("-"in number[-1])or("." in (number[0] or number[-1]))or(".." in number)or(".." in listdot):
            count=None
        elif ("0" in number[i]) or ("1"in number[i]): 
            count+=1
    
    return count

def getNumberOfDigitsOctal(number):
    count=0     
    listdot=" "
    listothers=""
    for i in range(len(number)):
        if(number[i]=="."):
            listdot+=number[i]
            
        if not(number[i]=="0" or number[i]=="1" or number[i]=="2" or number[i]=="3" or number[i]=="4" or number[i]=="5" or number[i]=="6" or number[i]=="7" or number[i]=="." or number[i]=="-"):
            listothers+=number[i]
        
        if("-." in number)or (len(listothers)>0)or("-"in number[1:-1])or("-"in number[-1])or("." in (number[0] or number[-1]))or(".." in number)or(".." in listdot):
            count=None
        elif ("0" in number[i]) or ("1"in number[i]) or ("2"in number[i]) or ("3"in number[i]) or ("4"in number[i]) or ("5"in number[i]) or ("6"in number[i]) or ("7"in number[i]): 
            count+=1
    
    return count

def getNumberOfDigitsHexadecimal(number):
    count=0     
    listdot=" "
    listothers=""
    for i in range(len(number)):
        if(number[i]=="."):
            listdot+=number[i]
            
        if not(number[i]=="0" or number[i]=="1" or number[i]=="2" or number[i]=="3" or number[i]=="4" or number[i]=="5" or number[i]=="6" or number[i]=="7" or number[i]=="8" or number[i]=="9"or number[i]=="A" or number[i]=="B" or number[i]=="C" or number[i]=="D" or number[i]=="E" or number[i]=="F" or number[i]=="." or number[i]=="-"):
            listothers+=number[i]
        
        if("-." in number)or (len(listothers)>0)or("-"in number[1:-1])or("-"in number[-1])or("." in (number[0] or number[-1]))or(".." in number)or(".." in listdot):
            count=None
        elif ("0" in number[i]) or ("1"in number[i]) or ("2"in number[i]) or ("3"in number[i]) or ("4"in number[i]) or ("5"in number[i]) or ("6"in number[i]) or ("7"in number[i]) or ("8"in number[i]) or("9"in number[i])or("A"in number[i])or("B"in number[i])or("C"in number[i])or("D"in number[i])or("E"in number[i])or("F"in number[i]): 
            count+=1
    
    return count
print("[Decimal] tiene", getNumberOfDigitsDecimal("-.10.0955"), "digitos")
print("[Binary] tiene", getNumberOfDigitsBinary("1001"), "digitos")
print("[Octal] tiene", getNumberOfDigitsOctal("141"), "digitos")
print("[Hexadecimal] tiene", getNumberOfDigitsHexadecimal(".-1081A"), "digitos")
"""
#EJERCICIO7
7. Diseñe un método llamado isPrime que reciba un número entero positivo mayor
que 0 como parámetro. El método debe devolver True si el número es primo o False si
no primo. Si el parámetro no es válido, el método debe devolver Ninguno
"""

def es_numero_primo(numero):    
    es_primo = True
    
    for i in range(2,numero):
        if numero%i==0:
            es_primo = False
                
    return es_primo
    
numero=int(input("Introduce un numero: "))
if numero > 0:
    print(es_numero_primo(numero))
else:
    print(None)
    

"""
#EJERCICIO8
8. Diseñe un método llamado solveSecondOrderEquation que reciba tres enteros
números positivos correspondientes a los coeficientes de una ecuación de segundo orden
(ax2+bx+c=0) y calcula sus posibles soluciones. Si los parámetros no son válidos, el
El método debe devolver Ninguno.
"""
def solveSecondOrderEquation(a, b, c):
    x=0
    y=0
    valid=[0,1,2,3,4,5,6,7,8,9]
    if (a not in valid) or (b not in valid) or (c not in valid) or (a <=0)or (b <=0)or (c <=0):
        x=None
        y=None  
    else:
        x1=(b**2)-(4*a*c)
        x3=x1**(1/2)
        x2=(b)+(x3)
        x=x2/(2*a)
        y1=(b**2)-(4*a*c)
        y3=y1**(1/2)
        y2=(b)-(y3)
        y=y2/(2*a)
    return x, y   
 
 

print(solveSecondOrderEquation(1,3,2))
print(solveSecondOrderEquation(6,5,1))
print(solveSecondOrderEquation(0,0,1))
"""
#EJERCICIO9
9. Diseñe un método llamado getPrimeDivisors que reciba un número positivo como
parámetro y devuelve una lista que contiene sus divisores primos. Si el parámetro no es válido
el método debe devolver Ninguno.        
"""
def isPrime(number):
    is_prime=True
    
    for i in range(2, number):
        if number%i==0:
            is_prime=False
   
        
    return is_prime

def getPrimeDivisors(number):
    divisors=[]
    count=0
    count2=1
    if number<0:
        divisors=None
    else:
        if isPrime(number):
            divisors=[1, number]
        else:
            while count<=2:
                if isPrime(count2) and number%count2==0:
                    divisors.append(count2)
                    count+=1
                count2+=1
        
    return divisors

print(getPrimeDivisors(2))
print(getPrimeDivisors(200))
print(getPrimeDivisors(65))
 
"""
EJERCICIO10
10. Diseñe un método llamado isFriendNumber que reciba dos números positivos y
devuelve True si los números son amigos, False en caso contrario. dos numeros son
considerados amigos si la suma de sus divisores, excepto el número dado, es igual
al segundo y viceversa.
"""
n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce otro numero: "))
x = 1
suma = 0
while x < n1:
    if n1 % x == 0:
        suma = suma + x
    x = x + 1
if suma == n2:
    print(True)
else:
    print(False)
