/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo
y mostrarlos
con Joptionpane
 */
package Ciclos04;

import javax.swing.JOptionPane;

public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba un numero: "));
        while(numero >= 0) {
            JOptionPane.showMessageDialog(null, "El numero "+numero+" es Positivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado "+conteo+" numeros que no son negativos");
    }
}    
