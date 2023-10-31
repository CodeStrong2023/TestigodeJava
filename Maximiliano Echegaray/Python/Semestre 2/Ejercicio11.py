#Ejercicio 11: crear una agenda telefonica
agenda = {}
while True:
    print('\t.:MENU.:')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Escriba una opcion de menu: '))
    if opcion == 1:
        nombre = input('Escriba el nombre del contacto: ')
        telefono = input('Escriba el telefono del contacto: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente!')
        else:
            print('Este contacto ya existe')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto')
        else:
            print('Este contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    else :
        print('Se equivoco de opcion de menu')
    print()
         