#Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10.

numero = int(input("Escriba un numero: "))
lista = [] #Creamos lista vacia
for i in range(1, 11):
    lista.append(i*numero)
    
print(f"\nTabla de multiplicar del {numero}: \n {lista}")

for indice, i in enumerate(lista):
    print(f"{numero} x {i} - {lista[indice]}") #Este ciclo es para ver el formato de una tabla de multiplicar