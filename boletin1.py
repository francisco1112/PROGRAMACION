"""1. Calcular el resultado de las siguientes expresiones lógicas:
from future.backports.test.pystone import TRUE"""

#a)false
print(7>=27 and not (7<=2))

#b)true
print(24>5 and 10<=10 or 10==5)

#c)false
print((10>=15 or 23==13) and not(8==8))

#d)true
print (not (6/3>3) or 7>7)

"""2. Calcular el valor de las siguientes expresiones aritméticas:"""
#a)
print(27%4+15/4, type(27%4+15/4))

#b)
print(37/4**2-2, type(37/4**2-2))

#c)
print(9*2/3*10*3, type(9*2/3*10*3))

#d)
print((7*3-4*4)**2/4*2, type((7*3-4*4)**2/4*2))


""" 3. Escribir una expresión lógica que cumpla:"""
#a)
precio = 60
print(60 <= precio and precio<=420)

precio = 420
print(60 <= precio and precio<=420)
#b)
precio=21 
print(precio % 2==1)

precio=40
print(precio % 2==1)  
#c)
saldo=200
dineroSacar=100
print(dineroSacar <= saldo and saldo >= 0 and dineroSacar > 0)

#d)
hora=23
minutos=22
minutos=60
hora=24
print(hora>=0 and hora<=23 and minutos<=59 and minutos>=0)

#e)
#con el or
estadoCivil='S'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
estadoCivil='S'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
estadoCivil='S'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
estadoCivil='S'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
estadoCivil='Ñ'
print(not(estadoCivil== 'S' or estadoCivil == 'C' or estadoCivil=='V' or estadoCivil=='D'))
#con el and
estadoCivil='D'
print(estadoCivil!= 'S' and estadoCivil!='C' and estadoCivil!='V' and estadoCivil!= 'D')

"""4. Escribir una expresión lógica que cumpla:"""
#a)
cantidad = -1
print(not(cantidad<0 or cantidad>300)) 
cantidad = 0
print(not(cantidad<0 or cantidad>300)) 
cantidad = 200
print(not(cantidad<0 or cantidad>300)) 

#b)
edad = 17
print(not(edad>=16 and edad<=22))
edad= 24
print(not(edad>=16 and edad<=22))

#c)
respuesta='S' 
print(respuesta!='S' and respuesta!='N')
respuesta='A'
print(respuesta!='S' and respuesta!='N')     
respuesta='N'  
print(respuesta!='S' and respuesta!='N') 
   
#d)
numero= 21
print(not(numero%7==0 or numero%3==0))
numero=15
print(not(numero%7==0 or numero%3==0))
numero=14
print(not(numero%7==0 or numero%3==0))
numero=16
print(not(numero%7==0 or numero%3==0))
      
 """ 5. Escribir la tabla de verdad para las siguientes expresiones lógicas:"""
#a)

a, b=True, True
print((a or b)and not(a))

a, b=True, False
print((a or b)and not(a))

a, b=False, True
print((a or b)and not(a))

a, b=False,False
print((a or b)and not(a))

#b)

a, b=True, True
print(not(a or b)and b)

a, b=True, False
print(not(a or b)and b)

a, b=False, True
print(not(a or b)and b)

a, b=False,False
print(not(a or b)and b)

#c)

a, b=True, True
print(a or not(b))

a, b=True, False
print(a or not(b))

a, b=False, True
print(a or not(b))

a, b=False, False
print(a or not(b))

#d)

a, b=True, True
print(not(a and b)and(b or a))

a, b=True, False
print(not(a and b)and(b or a))

a, b=False, True
print(not(a and b)and(b or a))

a, b=False, False
print(not(a and b)and(b or a))
     
      
      
      