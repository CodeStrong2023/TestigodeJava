#Definimos una funcion 
def mi_funcion():
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion()    #Llamando a la funcion
mi_funcion()    #Se puede llamar N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) #Pasamos uno por uno los fatos de la lista a la funcion
show(*person)   #Esto es lo mismo que lo anterior pero pasamos todo junto
person2 = ("Osvaldo", "Giordanini") #Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break #Esta es la unica manera que no se ejecute el Else
else:
    print('Esto se termina')
    
# List comprension, lista de comprension
names = ["Paolo","Rodrigo","Lupe","Pepe"]
alongP = [p for p in names if p[0] == 'P'] #Esto es una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}]

Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos lo que ven a traves del canal de Youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

#La palabra Return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b = 0):    #Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funcioness
def listarNombres(*nombres):    #Normalmente se utiliza: *args
    for nombre in nombres:  #Se va a convertir en tupla
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos): #Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items():   # kwargs significa : Key word argument
        print(f'{llave} : {valor}')
        
listarTerminos() #No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')
listarTerminos(Nombre='Lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10, 11) #No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos en una tupla
desplegarNombres([22, 55]) #La convertimos en una lista 

# Funciones recursivas
def factorial(numero):
    if numero == 1: #caso base
        return 1
    else:
        return numero * factorial(numero-1) #Caso recursivo
numeroFactorial = int(input('Escriba el numero para calcular el factorial: '))
resultado = factorial(numeroFactorial) #Lo hacemos en codigo duro
print(f'El factorial del numero es: {numeroFactorial} es: {resultado}') #Tarea para que el usuario ingrese el num