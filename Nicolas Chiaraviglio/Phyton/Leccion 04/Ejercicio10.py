"""Ejercicio10: No repetir caracteres
Hcaer un programa que pida una cadena por teclado,Luego
meter los caracteres en unalista sin repetir caracteres.
"""
cadena=input("Digite una cadena: ")
lista=[]
for i in cadena:
    if i not in lista: #Si elcaracter aun no esta en la lista
        lista.append(i)#Lo agregamos a la lista
print(f"\nLista de caracteres sin repetir ninguno: \n {lista}")