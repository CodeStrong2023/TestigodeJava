/*
Ejercicio 7: PEdir numero hasta que se introduzca uno negativo
y calcular la media
 */
package Ciclos07;

import javax.swing.JOptionPane;


public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, conteo = 0,suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba un numero: "));
        while(numero >= 0){ //Mientras numero no sea negativo
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Escriba otro numero: "));
        if(conteo == 0){
            JOptionPane.showMessageDialog(null, "\nError, la division entre cero no existe");
        }
        else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "El promedio es: "+promedio);
        }
        }
    }
}
