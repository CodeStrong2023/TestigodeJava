#Ejercicio 2 : Modificar los elementos de una lista 
#Llenar una lista como los numero del 1 al 10,luego modificar los
#elementos de la lsita multiplicadolos por un valor ingresado por el usuario
lista= list(range(1,11))
print('Lsita Original')
for i in lista:
    print(i, end= '-')
valor=int(input('\nDigite un valor a multiplicar:'))
#Multiplicamos todos los elementos de la lista 
for indice, i in enumerate(lista): #Funcion para modificar indices de la lista
    lista[indice] *=valor# El iterador solo recorre los indices,En esta linea se multiplican
    
print(f'Lista final con los elementos multiplcados por {valor}')
for i in lista:
    print(i, end= '-')