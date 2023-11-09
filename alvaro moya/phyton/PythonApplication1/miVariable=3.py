""""
miVariable=3 
print(miVariable)
miVariable=4
print(miVariable)
miVariable=3.5
print(miVariable)
x=10
y=2
z=x+y
print(id(x))
print(id(y))
print(id(z))


a=10.78
print(type(a))
x=14.5
print(x)
print(type(x))
x="hola profe"
print(x)
print(type(x))
x=True
print(x)
print(type(x))
x=False
print(x)
print(type(x))

# manejo de cadenas (string)
miGrupoFavorito="Los Testigos de Java"
caracteristicas="The Best Group Programation"
print("mi grupo favorito es:" + miGrupoFavorito + ", "  + caracteristicas)

numero1="7"
numero2="8"
print(int(numero1) + int(numero2))

# tipos booleanos (bool)
miBooleano=3>2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
    
else:
    print("El resultado es Falso")
    

#procesar la entrada de usuario
#funcion input
## resultado=input("Digite un numero: ") # regresa un dato tipo string
## print(resultado)

#conversion de la entrada de datosç
numero1=int (input("escribe el primer numero: "))
numero2=int (input("escribe el segundo numero: "))
resultado=numero1 + numero2
print("el resultado de la suma es: ", resultado)
"""
""""
operandoA= 8
operandoB= 5
suma=operandoA + operandoB
#print("el resultado de la suma es: ", suma)
print(f'el resultado de la suma es: {suma}')

resta= operandoA - operandoB
print(f'El resultado de la resta es: {resta}')


multiplicacion=operandoA * operandoB
print(f'el resultado de la multiplicacion es: {multiplicacion}')

division=operandoA / operandoB
print(f'el resultado de la division es: {division}')

exponente=operandoA ** operandoB
print(f'el resultado del ezponente es: {exponente}')
"""
""""
alto=int(input("proporciona el alto del rectangulo: "))
ancho=int(input("proporciona el ancho del rectangulo; "))
area=alto * ancho 
perimetro=(alto + ancho) * 2
print("area: ", area)
print("perimetro: ", perimetro)

"""

"""
miVariable3=10
print(miVariable3)

#operadores de reasignacion

miVariable3=miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

miVariable3 -= 2
print(miVariable3)

miVariable3 *= 3
print(miVariable3)


miVariable3 /=2
print(miVariable3)

"""

"""
#operadores de comparacion

d=4
b=2
resultado= d==b
print(resultado)

#operador diferente
resultado=d != b 
print(resultado)

#operador mayor que
resultado=d > b
print(resultado)

#operador menor que
resultado=d < b
print(resultado)

#operador meno o igual que
resultado=d <= b 
print(resultado)

#operador mayor o igual que
resultado=d >= b
print(resultado)
"""

"""
a=int(input("digite un numero: "))
print(f'el residuo de la division es: {a % 2 } ')
if a % 2 ==0:
    print(f'El valor de a es: {a} es un numero PAR')
else:
    print(f'El valor de a es: {a} es un numero IMPAR')
    
"""
"""
edadAdulto=18
edadPersona=int(input('digite su edad: '))
if edadPersona >= edadAdulto:
    print(f'su edad es: {edadPersona} años, usted es mayor de edad')
else:
    print(f'su edad es; {edadPersona} años, usted es menor de edad'

"""
   
""" 
#operadores logico
a=False
b=False
resultado=a and b
print(resultado)    

#operador or
resultado=a or b
print(resultado)

#operador not
resultado= not a 
print(resultado)


#ejercicio valor dentro de un rango
valor=int(input('digite un numero: '))
valorMinimo=0
valorMaximo=5
dentroRango=(valor>= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f'el valor {valor} esta dentro del rango')
else:
    print(f'el valor {valor} no esta dentro del rango')


#ejercicios con el operador or, operador not
vacaciones=False
diaDescanso=True
if not(vacaciones or diaDescanso):
    print('puede asistir al juego')
else:
    print('tiene trabajo por hacer')

#Ejercicio: rango entre 20 y 30 años
edad=int(input('dijite su edad: '))
veinte= edad >= 20 and edad <30
treinta= edad>=30 and edad <40
print(treinta)
if veinte or treinta:
 print('estas dentro del rango de los (20/`0) a (30/0)')
else:
    print('no estas dentro del rango de los (20/0) a (30/0)')

#Ejercicio: el mayor de dos numeros
numero1=int(input('digite el valor para el numero1: '))
numero2=int(input('digite el valor para el numero2: ')) 
if numero1 > numero2:
    print('el numero 1 es mayor')
else:
    print('el numero 2 es mayor ')   

#Ejercicio tienda de libro
print("digite los siguientes datos del libro")
nombre=input("Digite el nombre del libro: ")
ID=int(input("Digite el ID del libro: "))
Precio=float(input("Digite el precio del libro: "))    
envioGratuito=input("indicar si el libro es gratuito (true/false): ")
if envioGratuito=='True':
    envioGratuito=True
elif envioGratuito=='False':
    envioGratuito=False
else:
    envioGratuito='el valor ingresado es incorrecto, debe escribir true/false '
print (f'''
    nombre: {nombre}
    Id: {ID}
    precio {Precio}
    envio gratuito? {envioGratuito}
''')
"""

