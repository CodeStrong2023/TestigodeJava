
import java.util.Scanner;


public class CLase6 {

    public static void main(String[] args) {
        //Conversion de tipos primitivos
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);

        // pedir un valor
        var entrada = new Scanner(System.in);
        System.out.println("Ingrese su edad:");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println(" = " + edad);
        
        //conversion parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(4);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Escriba un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
    }
}
