"""Ejercicio 3:Funcion Recursiva
Imrpimir números de 5 a 1 de manera descendente usando funciones recursivas
Puede ser cualquier valor positivo,Por ejemplo,si pasamos el
valor de 5,debe imprimir:
5
4
3
2
1
En caso de ser el número 3 debe imprimir:
3
2
1
Si se ingresan números negativos no imprime nada"""

def imprimir_numeros_recursivos(numero):
    if numero >= 1: # caso Base
        print(numero)
        imprimir_numeros_recursivos(numero-1)#Caso recursivo
    elif numero==0:
        return

    elif numero<=0:
        print("Valor ingresado incorrecto...")


imprimir_numeros_recursivos(int(input("Ingresa numero que decee hacer recursivo:")))#Tarea:que el usuario ingrese el numero