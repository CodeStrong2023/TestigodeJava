
import java.util.Scanner;


public class Clase10 {
    public static void main(String[] args) {
        //condicional if and else
        
        /*var condicion = true;
        if(condicion) {
            System.out.println("Condicion verdadera"); //condicion simple
        }
        else{
            System.out.println("Condicion Falsa"); //condicional doble
        }*/
        
        
        
        //sentencia de control switch
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escriba un numero del 1 al 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch(numero) {
            case 1:
                numeroTexto = "Numero uno";
                break;
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break;
            case 4:
                numeroTexto = "Numero cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }
}
