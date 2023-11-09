/*
Ejercicio 5: Realizar un juego para adivinar un numero, para ello generar numero aleatorio entre 0 y 100 e ir pidiendo numeros si es menor o mayor respecto a n
 */
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //genera num aleatorio
        do{
            System.out.println("Escriba un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Escriba un numero mayor");
            }
            else if(numero > aleatorio){
                System.out.println("Escriba un numero menor");
            }
            else {
                System.out.println("Felicidades, !!haz adivinado el numero!!");
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: "+conteo+" intentos");
    }
}
