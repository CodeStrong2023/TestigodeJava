"""
Ejercicio 2 :
Funcion con *arg para multiplicar los valores recibidos
de tipo númerico,utilizando argumentos variables*args
como parametro de la función y regresar como resultado
la multiplicacion de todos los valores pasados como argumentos
"""

#Definimos la funcion para multiplicar
def multiplicar_valores (*numeros):#El mas utilizando es *args
    resultado= 1 #El cero no nos ayuda a multiplicar
    for numero in numeros:
        resultado*=numero
    return resultado

#LLamamos a la función
print(multiplicar_valores(3,5,15,3))#Le pasamos los argumentos
