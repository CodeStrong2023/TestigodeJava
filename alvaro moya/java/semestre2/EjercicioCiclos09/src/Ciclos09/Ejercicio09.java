/*
Ejercicio 9: Pedir dia,mes y año de fecha e indicar si es correcta
Suponiendo que todos los meses tienen 30 dias
 */
package Ciclos09;

import javax.swing.JOptionPane;


public class Ejercicio09 {
     public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Escriba el dia: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Escriba el mes: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Escriba el año: "));
        if((dia != 0)&&(dia <= 30)) {
            if((mes != 0)&&(mes <= 12)) {
                if((anio != 0)&&(anio <= 2022)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else{
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto" );
                }
            }else{
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
            }
        }else{
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, dia incorrecto");
        }
    }
}
