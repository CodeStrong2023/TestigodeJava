#Ejercicio 01: Crear funcion para sumar valores recibidos de tipo numericos
def sumar_valor(*args): #Recibimos una cantidad de parametros indefinidos
    resultado = 0
    #iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado

#Llamamos a la funcion
print(sumar_valor(3, 5, 9, 2, 1))