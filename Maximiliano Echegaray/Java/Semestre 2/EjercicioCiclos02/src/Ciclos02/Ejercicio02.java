/* Ejercicio 2: leer numero e indicar si es positivo o negativo hasta introducir 0
*/

package Ciclos02;

import java.util.Scanner;

public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escriba un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0){
            if(numero > 0){
                System.out.println("El numero "+numero+" es POSITIVO");
            }
            else {
                System.out.println("El numero "+numero+" es NEGATIVO");
            }
            System.out.println("Escriba otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
