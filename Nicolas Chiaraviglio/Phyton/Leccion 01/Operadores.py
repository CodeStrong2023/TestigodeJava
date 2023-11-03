#OPERADORES

operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("Resultado de la suma: ", suma)
print(f"El resultado de la suma es: {suma}")#"f" de formato#interpolacion(incluimos la variable en una cadena con las llaves y la "f")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")#nos va a devolver como resultado un numero entero

modulo = operandoA % operandoB
print(f"El resultado del residuo de la division es: {modulo}")
    
exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")


#EJERCICIO AREA DEL RECTANGULO

alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("Area: ", area)
print("Perimetro: ", perimetro)

#Asignacion y Comparacion
#Asignacion

miVariable3 = 10
print(miVariable3)
miVariable3 = miVariable3 + 1
print(miVariable3)#incremento con reasignacion#se reasigna el valor de la variable en este caso con una suma

miVariable3 += 1
print(miVariable3)#se reasigna igualmente el valor de la variable pero de forma mas resumida

miVariable3 -= 2
print(miVariable3)

miVariable3 *= 3
print(miVariable3)

miVariable3 //= 2
print(miVariable3)

#Comparacion
#iguales
d = 4
b = 2
resultado = d == b#comprobamos si son iguales #siempre por prioridad se evalua el lado derecho, o en su defecto el parentesis
print(resultado)#FALSE
#diferentes
resultado = d != b#comprobamos si son diferentes
print(resultado)
#mayor que
resultado = d > b
print(resultado)
#menor que
resultado = d < b
print(resultado)
#menor/mayor o igual
resultado = d <= b
print(resultado)
resultado = d >= b
print(resultado)

#EJERCICIO NUMERO PAR O IMPAR

a = int(input("Digite un numero: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero PAR")
else:    
    print(f"El valor de a es: {a} es un numero IMPAR")

#EJERCICIO: DETERMINAR SI ES MAYOR DE EDAD

b = int(input("Ingrese su edad: "))
print(f"Su edad es: {b}")
if b >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")


#OPERADORES LOGICOS: AND, OR O NOT
#AND
a = True
b = True
resultado = a and b
print(resultado)

#OR
a = False
b = True
resultado = a or b
print(resultado)

#NOT
a = False
resultado = not a
print(resultado)#los otros dos operadores necesitan de dos operandos para trabajar, el operador not es unario, necesita de uno solo, nos arroja el resultado "opuesto"

#EJERCICIO: VALOR DENTRO DE UN RANGO

a = int(input("Ingrese un numero: "))
rango = (a >= 0 and a <= 5)
if rango:
    print(f"El valor {a} esta dentro del rango")
else:
    print(f"El valor {a} esta fuera del rango")

#EJERCICIO: OPERADOR OR

vacaciones = True
diaDescanso = False
if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")#al ser ya uno verdadero, es true

#EJERCICIO RANGO ENTRE LAS EDADES 20 Y 30 AÑOS

edad = int(input("Digite su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)
 
if veinte or treinta:
    if veinte:    
        print("Estas dentro del rango de los (20'0) años")#if dentro de if, anidacion
    elif treinta:
        print("Estas dentro del rango de los (30'0) años")
else:
    print("No estas dentro del rango de los (20'0) a los (30'0) años") 
# Seria lo mismo decir if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):, incluso se puede simplificar ams la sintaxis

#EJERCICIO: EL MAYOR DE DOS NUMEROS

valor1 = int(input("Inserte valor para el valor1: "))
valor2 = int(input("Inserte valor para el valor2: "))

if valor1 > valor2:
    print(f"El valor que es mayor es: {valor1}")
else:
    print(f"El valor que es mayor es: {valor2}")

#EJERCICIO: TIENDA DE LIBROS

print("             INGRESE LOS SIGUIENTES DATOS DEL LIBRO              ")
nombre = input("Digite el nombre del libro: ")
iD = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indique si el envio es gratuito (True/False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir: True/False "

print(f"""
        Nombre: {nombre}
        ID: {iD}
        Precio: {precio}
        Envio Gratuito ?: {envioGratuito} 
""")






