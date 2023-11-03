#IF/ELSE

condicion = True
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion sin especifir")

#Convercion de numero a texto

num = int(input("Digite un numero en el rango del 1 al 3: "))
numTexto = ""
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
    numTexto = "Numero 2"
elif num == 3:
    numTexto = "Numero 3"
else:
    numTexto = "Has ingresado un numero fuera de rango"
print(f"El numero ingresado es: {num} - {numTexto}")

#EJERCICIO: ESCRIBIR EXPRECION ALGORITMICA

a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
c = float(input("Digite el valor de c: "))
resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
print(f"El resultado es: {resultado}")

#OPERADOR TERNARIO

condicion = False
print("Condicion Verdadera") if condicion else print ("Condicion Falsa")#no se debe utilizar elif#no se aconseja en codigos largos complejos

#CICLO WHILE(MIENTRAS)#SE VA A REPETIR SIEMPRE Y CUANDO LA CONDIDICON SEA VERDADERA

contador = 0
while contador < 78:
    print("Ejecutamos nuestro ciclo while", contador)
    contador += 1
else:
    print("Fin del ciclo while")

#EJERCICIOS CICLO WHILE1

maximo = 5
contador = 0
while contador <= maximo:
    print(f"Unidad numero: {contador}")
    contador += 1

#EJERCICIO CICLO WHILE2

minimo = 1
contador = 5
while contador >= minimo:
    print(f"Unidad numero: {contador}")
    contador -= 1
else:
    print("FIN DEL CONTEO.")

#CICLO FOR(PARA)#NOS PERMITE ITERAR(RECORRER) UNA LISTA DE DATOS O ELEMENTOS

cadena = "HELLO"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")

#PALABRA RESERVADA BREAK

for letra in "Alemania":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break#break rompe el ciclo y termina, sin siquiera llegar al else
else:
    print("Fin del ciclo for")

#PALABRA RESERVADA CONTINUE

for i in range(6):#rango de numeros, sin incluir el 6 en este caso, ya que toma 6 digitos desde el 0
    if i % 2 == 0:
        print(f"Valor: {i}")

for i in range(6):
    if i % 2 != 0:#cuando el resto de la divicion por 2 sea DISTINTA de 0
        continue#eludir o anular todos los numeros que sean impares, en este caso
    print(f"Valor: {i}")
















