
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona();   //llamamos al contructor
        persona1.nombre = "Ariel";
        persona1.apellido = "Betancud";
        persona1.obtenerInformación(); 
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = "+persona2);
        System.out.println("persona1 = "+persona1);
        persona2.obtenerInformación();
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformación();
    }
}
