#Ejercicio 4: Sumar numeros pares dentro de un rango
# Hacer un programa para sumar numeros pares dentro de un rango,por ej:
#                                                               Suma de pares del 2 al 30
#                                                               Suma = 240
a = int(input("Escriba de donde va a comenzar la suma: "))
b = int(input("Escriba hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a, b+1):
    if i % 2 == 0: #Esto es si el numero es par
        suma += i
print(F"\nLa suma de numeros pares dentro del rango es: {suma} ")