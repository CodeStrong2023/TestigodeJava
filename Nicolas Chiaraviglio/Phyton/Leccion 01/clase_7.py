# ciclo while (mientras o durante)
"""
contador = 0
while contador < 3:
    print('Ejecutamos el ciclo while ', contador)
    contador += 1
else:
    print('Fin del ciclo while')"""

#ciclo for
"""
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')"""

# Palabra reservada Break
"""
for letra in 'Alemania':
    if letra =='a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin del ciclo for')"""

#Palabra reservada continue

for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')

