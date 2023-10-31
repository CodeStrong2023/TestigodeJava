/*
Ejercicio 5: Realizar un juego para adivinar un numero, para ello generar numero aleatorio entre 0 y 100 e ir pidiendo numeros si es menor o mayor respecto a n
con Joptionpane
 */
package Ciclos05;

import javax.swing.JOptionPane;


public class Ejercicio05 {
    public static void main(String[] args) {
        
    
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //genera num aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba un numero: "));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Escriba un numero Mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Escriba un numero Menor");
            }
            else {
                JOptionPane.showMessageDialog(null, "!!Felicidades!!! HAs adivinado el numero");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en : "+conteo+" intentos");
    }
}