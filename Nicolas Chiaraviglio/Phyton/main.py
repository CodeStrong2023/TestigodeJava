"""Lista=Ariel,Liliana,Natalia,Osvaldo"""
#Colecciones en Python

#Las listas es lo que se conoce en otros lenguajes como arreglos o vectores
nombres=['Naty','Osvaldo','Lyli','Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

#Recuperar rangos de la lista
print(nombres)
print(nombres[0:2])#Solo muestra el indice 0,1 pero no el indice 2
#ir al inicio de la lista al indice(Sin incluirlo)
print(nombres[ :3])#Indices a mostrar 0,1,2
#Desde el indice indicado hasta el final@
print(nombres[1: ])
#Modificar un valor dentro de nuestra lista 
nombres[2]='Liliana'
nombres[0]='Natalia'
print(nombres)
#Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista ')
#Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

#Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)
#Insertar un elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print (nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)
#Eliminar el ultimo elemento
nombres.pop()
print(nombre)

#Eliminar un indice especifico
del nombres [2] #Del significa delete (eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos 
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
#print(nombres)

#Definimos una tupla
cocina = ('Cuchara','cuchillo','tenedor')
print(len(cocina))
#Acceder a un elemento, para estp ulizamoscorchetes no parentesis
print(cocina[0])
#Mostrar de manera inversa
print(cocina[-1])
#Acceder a un rango
print(cocina[0:2])
#Ejemplo
Verduras=('papa')#Una tupla necesita aunque sea de un elemento :la coma
# de lo contrario solo sera un tipo str cadena

#Recorremos los elementos de la tupla 
for cocinar in cocina:
    print(cocinar, end=' ') # Print esta usando \n para saltos de linear

cocinaLista=list(cocina)
cocinaLista[0]='Plato'
cocina=tuple(cocinaLista)
print('\n',cocina)

#del cocina esto es para eliminar 
#Tipo set
planetas= {'Marte','Jupiter','Venus'}
print(len(planetas))#Usamos la funcion len = length sigfica largo
#Revisar si un elemento existe dentro de set
print('Jupiter'in planetas)

#Agregar un elemento
planetas.add('Tierra') #add es una funcion
print(planetas)
#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter')#Esta funcion ante un mal ingreso da error
print(planetas)
planetas.discard('tierra')#Esta funcion no nos presenta ningun tipo de error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
#print(planetas)# al eliminar nos muestra un error

# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
#dict (key,value)
diccionario={
    'IDE':'Integrated Development Enviroment',
    'POO':'Programacion orientada a Objetos',
    'SABD':'Sistema de adminitracion de Base de Datos'
}
print(len(diccionario))
print(diccionario)
#Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])
#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))
#Modificamos elementos
diccionario['IDE']='Entorno de Desarrolo Integrado'
print(diccionario)

#Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)
for termino , valor in diccionario.items():
    print(termino,valor)

#Otras maneras de accerder al diccionario
for termino in diccionario.keys(): #Estamos usando una funcion
    print(termino) #Muestra solo las llaves

for valor in diccionario.values():
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE'in diccionario)#Devuelve un boleeano

#Agregar un elemento
diccionario['PK']='Primaty Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario #El diccionario se borro 

#Concatemanos listas
lista1= [1,2,3,1]
lista2= [4,5,6,1]
lista3=lista1+lista2 #Concatenamos
print(lista3)

lista3.extend([7,8,9,1])#Funcion para agregar varios elmentos auna lista
print(lista3)
print(lista3.index(5)) #Funcion para ubicar en que indice esta el valor ingresado
#print(lista.index(0))#esto daria un error por no ser el elemento parte de la lista 
#Como saber cuantos valores repetidos hay dentro de una lista 
print(lista3.count(1))

#Para poner al reves una lista
lista3.reverse()
print(lista3)


#Para que una lista se multiplique repitiendo sus elementos
lista3=lista3 * 2
print(lista3)

#Metodos de ordenamiento,es una funcion
lista3. sort()#Ordena los elementos en forma ascendente
print(lista3)
lista3.sort(reverse=True)#Orden descendentemente
print(lista3)
#Repaso de tuplas
tupla=(4, 'Hola', 6.78, [1,2,78],4,'Hola')#Puede tener diferentes tipos de datos dentro
print(tupla)
print(4 in tupla)#Accion booleana , su respuesta esde tipo boolean
#Lo que podemos usar dentro de tuplas son: index, count, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla
#Repaso de set o conjunto
#para definir un conjunto
conjunto2= set()
conjunto1= {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1)# Preguntamos si  el numero 3 No esta en el conjunto 1

#Como hacer la igualdad de dos conjuntos
print (conjunto1==conjunto2)# Nos devuelve como respuesta un booleano

#Operaciones en conjunto
conjunto3 = conjunto1 | conjunto2 #La linea une los dos conjuntos
print(conjunto3)

conjunto3 =conjunto1 & conjunto2 #Que elementos tiene en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Asigna el valor que esta en el conjunto 1 y no en el conjunto 2
print(conjunto3)

conjunto3= conjunto2 - conjunto1
print(conjunto3)

conjunto3= conjunto1 ^ conjunto2 #Elementos que no comparten o que son difetes entre ambos
print(conjunto3)

conjunto3= conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))# Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2))# Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#Como saber si ambos conjuntos son dosconexos,esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

#Con vertit un conjunto totalmente en inmutable
conjunto1=frozenset #Esto hace que el conjunto sea totalmente inmutable
#No se úede agregar, modificar ni eliminar elementos del conjunto 

#Repaso Diccionarios
diccionarioNuevo = {'Azul':'Blue','Rojo':'Red','Verde':'Green','Amarillo':'Yellow'}
print(diccionarioNuevo)
#Como eliminar
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferente tipos de datos 
diccionario2 ={'Ariel':{'Edad':40,'Altura':1.83},'Osvaldo':[45,1.85],'Natalia':[35,1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre':'Lionel Messi','Edad':35,'Altura':1.70,'Precio':'50 Millones','Posicion':'Extremo Derecho'},
    11: {'Nombre':'Angel Di Maria','Edad': 34, 'Altura': 1.80, 'Precio':'12 Millones', 'Posicion':'Extremo Derecho'},
    21: {'Nombre':'Paulo Dybala','Edad':28,'Altura':1.77,'Precio':'35 Millones','Posicion':'Media Punta'},
    19: {'Nombre':'Nicolás Otamendi','Edad':34,'Altura':1.83,'Precio':'3.5 Millones','Posicion':'Defensa Central'},
    1: {'Nombre':'Franco Armani','Edad':35,'Altura':1.89,'Precio':'3.5 Millones','Posicion':'Portero'},
    6: {'Nombre': 'Leandro Paredes', 'Edad': 29, 'Altura': 1.82, 'Precio': '12 Millones', 'Posicion': 'Centrocampista'},
    21: {'Nombre': 'Alexis McAllister', 'Edad': 24, 'Altura': 1.76, 'Precio': '40 Millones', 'Posicion': 'Centrocampista'},
    25: {'Nombre': 'Enzo Fernandez', 'Edad': 22, 'Altura': 1.78, 'Precio': '121 Millones', 'Posicion': 'Centrocampista'},
    8: {'Nombre': 'Rodrigo De Paul', 'Edad': 29, 'Altura': 1.80, 'Precio': '37 Millones', 'Posicion': 'Centrocampista'}
}
for llave, valor  in seleccionArgentina.items():
    print(llave,valor)
#Como tarea agregar por lo menos 4 jugadores mas al diccionario : seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de jugadores: ',end=' ')
print(len(seleccionArgentina))

#Pilas usando listas
pila=[1,2,3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop()#Quita el ultimo elemento y los guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi:{pila}')

#Colas con listas
#Estructura de datos de tipo fifo(first input/firs ourput)
cola=['Ariel','Osvaldo','Liliana','Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola 
seRetira=cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

#Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')


