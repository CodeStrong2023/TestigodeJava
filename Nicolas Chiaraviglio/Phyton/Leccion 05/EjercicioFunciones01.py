"""Ejercicio01:Crear un función para sumar los valores recibidos de tipo
númericos,utilizando argumentos variables * args como parametros de la 
Función y agregar como resultado la suma de todos los valores
como argumentos."""
def sumar_valor(*args):#Recibimos una cantidad de parámetros indefinidos
    resultado=0
    #Iteramos cada elemento
    for valor in args:
        resultado+=valor
    return resultado


#Llamamos a la funcion
print(sumar_valor(3,5,9,2,1))

