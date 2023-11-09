# Ejercicio 3: Funcion Recursiva
#Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
def imprimir_numeros_recursivos(numero):    #Caso base
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)   #Caso recursivo
    elif numero == 0:
        return 
    elif numero <= 0:
        print('Valor ingresado incorrecto...')
    
    
imprimir_numeros_recursivos(5)