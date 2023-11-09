/* Ejercicio 2: leer numero e indicar si es positivo o negativo hasta introducir 0
con optionpane*/

package Ciclos02;

import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba un numero: "));
        while (numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es positivo");
            }
            else {
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es negativo");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        JOptionPane.showMessageDialog(null, "El numero "+numero+" finaliza el programa");
    }    
}