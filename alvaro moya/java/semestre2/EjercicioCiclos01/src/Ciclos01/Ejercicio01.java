/* Ejercicio 1:  Leer numero u mostrar elevado al cuadrado, hasta que se introduzca un numero negativo*/
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0) {
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        System.out.println("El progtama a finalizado por numero negativo");
    }
}
