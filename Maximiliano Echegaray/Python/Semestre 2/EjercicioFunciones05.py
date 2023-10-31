# Ejercicio 5: Convertidor de temperaturas
#Realizar funciones para convertir grado celsius a fahrenheit y viceversa

# Funcion que convierte de celsius a farhenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 #La precedencia: * / +

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input('Escriba el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Escriba el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')