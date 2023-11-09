/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se aplique:
Variables: Evita cambiar el valor que almacena la variable
metodos: Evita que se modifique la definicion o el comportamiento de un metodo desde subclase (hija)
clases: Evita crear clases hija
*/
package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
        //miDni = 203131231; No se puede modificar
        //Persona.CONSTANTE_AQUI = 9; //No se puede modificar
        System.out.println("Mi atrinuto constante es: "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre = " + persona1.getNombre());
    }
}
