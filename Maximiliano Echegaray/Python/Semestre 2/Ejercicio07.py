#Ejercicio 7: Juego adivina el numero
# Debe generar numero aleatorio entre 1 y 100, e ir pidiendo numeros
# y si es menor o mayor hasta acertar al numero
import random
print("\t.:Juego Adivina el numero: .")
aleatorio = random.randint(0, 100) #Toma de 0 a 100, generamos num aleatorio
contador = 0
while True:
    numero = int(input("Escriba un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el numero, escriba un numero menor")
    elif numero < aleatorio:
        print("\tNo es el numero, escriba un numero mayor")
    else:
        print(f"FELICIDADES, acabas de adivinar el numero {aleatorio}")
        break #Rompre el ciclo y el bucle
print(f"\nNumero de intentos: {contador}")