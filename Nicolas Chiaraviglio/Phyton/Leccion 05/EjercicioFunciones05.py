"""Ejercicio 5 : Convertidor de temperaturas
Realizar dos funciones para convertir de grados elsius
a  fahrenheit y viseversa
Investigar las formulas

Funcion que convierte de elsius a fahrenheit"""
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 #La presedencia:multipliacion,division y suma

def fahrenheit_celsius(fahrenjeit):
    return (fahrenjeit-32)*5/9#Respetar la presedencia utilizando parentesis

celsius=float(input("Digite el valor de celsiues "))
resultado=celsius_fahrenheit(celsius)
print(f"{celsius} C a F -> {resultado:.2f}")

fahrenheit=float(input("Digite el valor de fahrenheit: "))
resultado=fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} F a C ->{resultado:.2f} ")