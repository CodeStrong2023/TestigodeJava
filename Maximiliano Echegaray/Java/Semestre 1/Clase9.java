package Ejercicio5;

import java.util.Scanner;
public class Clase9 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //float nota1,nota2,nota3,suma;
        
        //Guardamos las tres notas
        //System.out.println("Escriba las tres calificaciones");
        //nota1 = Float.parseFloat(entrada.nextLine());
        //nota2 = Float.parseFloat(entrada.nextLine());
        //nota3 = Float.parseFloat(entrada.nextLine());
        //suma = nota1 + nota2 + nota3;
        //System.out.println("\nLa suma es: "+suma);
        
        //Ejercicio6
        
        //float guillermo,luis,juan,total;
        //System.out.println("Escriba la cantidad de dinero de Guillermo: ");
        //guillermo = Float.parseFloat(entrada.nextLine());
        
        //luis = guillermo / 2;
        //juan =(luis + guillermo) / 2;
        //total = luis + guillermo + juan;
        //System.out.println("\nEl dinero de Luis es: US$"+luis);
        //System.out.println("El dinero de Juan es: US$"+juan);
        //System.out.println("El total de dinero entre los tres es: US$"+total);
        
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMensual, ventaCarro, porcVenta, totalPrecio;
        
        System.out.println("Escriba la cantidad de carros vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Escriba el precio de un carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine());
        
        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05f;
        salarioMensual = salario + comision + porcVenta;
        
        System.out.println("\nEl salario mensual es: "+ salarioMensual);
        
        
    }
}
