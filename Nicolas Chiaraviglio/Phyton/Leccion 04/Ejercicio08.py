"""Ejercicio 8 : Menu intereactivo - Cajero autamtico
Hacer un programa que simule un cajero automatico con un salgo inicial de 1000$
y tendra el siguiente menu de opciones:
1.Ingresar dinero en la cuenta
2.Retirar dinero de la cuenta
3.Mostrar dinero disponble
4.Salir"""

saldo=1000
while True:
    print("\t.:MENÚ:.")
    print("1.Ingresar dinero en la cuenta")
    print("2.Retirar dinero de la cuenta")
    print("3.Mostrar dinero disponible")
    print("4.Salir")
    opcion= int(input("Digite una opcion de menú: "))
    print()
    if opcion== 1:
        extra=float(input("Cuanto dinero desea ingrear ->  "))
        saldo += extra
        print(f"Dinero en la cuenta al momento: $ {saldo}")
    elif opcion ==2:
        retirar=float(input("Cuanto dinero desea retirar -> "))
        if retirar>saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: ${saldo} ")
    elif opcion ==3:
        print(f"Dinero en al cuenta al momento: ${saldo}")
    elif opcion ==4:
        print("Gracias por utilizar su cajero automatico,hasta pronto")
        break
    else:
        print("Error,se equivoco de opcion de menú")
        print()

