a: str = "Hola alumnos"#tipo string #: str, simplemente una referencia del tipo de dato que se desea que sea "a"
print(type(a))#type funcion que nos permite ver que tipo de dato es el que se almacena
b = 10.78
print(type(b))#tipo float
c = True
print(type(c))#tipo boolean
d = 8
print(type(d))#tipo int

# MANEJO DE CADENAS (String)

miGrupoFavorito = "Slipknot"
print("Mi grupo favorito es: "+miGrupoFavorito)
miComidaFavorita = "Pizza"+" "+"Una delicia"
print("Mi comida favorita es: "+miComidaFavorita)
caracteristicas = "La mejor banda de rock"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)#el uso de la coma es lo mismo que el uso de las comillas y el signo +

numero1 = "7"
numero2 = "8"
print(numero1 + numero2)#al ser variables de tipo string no las sumas, las concatena
print(int(numero1) + int(numero2))#transformamos el string a entero, y se suman, solo funciona si la variable string es con digitos

#TIPOS BOLEANOS (BOOL)

miBooleano = 3 > 2
print(miBooleano)

if miBooleano: 
    print("El resultado es verdadero")
else:
    print("El resultado es falso")
    #si o sino, if o else, condicionales

#PROCESAR LA ENTRADA DEL USUSARIO #funcion imput

resultado = input("Digite un numero: ")#regresa un dato tipo string
print(resultado)

#CONVERSION DE LA ENTRADA DE DATOS

numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultadod de la suma es: ", resultado)
#con la funcion "int" transformamos los datos de tipo "string" a enteros, por lo que se da la suma de las variables
















