/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo
y mostrarlos
 */
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Escriba un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0) {
            System.out.println("el numero "+numero+" es Positivo");
            conteo++;
            System.out.println("Escriba otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("A ingresado "+conteo+" numeros qie no son negativos");
    }
}
