/* Ejercicio 3: Leer numeros hasta que se introduzca un 0, Para cada numero indicar si es par o impar */
package Ciclos03;

import javax.swing.JOptionPane;


public class Ejercicio03 {
        public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba un numero"));
        while(numero !=0){
            if (numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba otro numero"));

        }
        JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" finaliza el programa");
    }
}