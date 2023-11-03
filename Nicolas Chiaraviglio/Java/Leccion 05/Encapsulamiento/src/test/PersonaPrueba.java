
package test;

import dominio.Persona;
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1= new Persona("Osvaldo", 57.000,false);
        
        //Modificar a través de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre="Juan Ignacio";//Ya no se puede utilizar
        //System.iut.println("Nombre es :"+persona1.nombre);//Error
        System.out.println("persona con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 con su sueldo modificado: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        //Tarea:Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir,luego modificar sus valores y volvera imprimir
        System.out.println("persona1: "+persona1.toString());
    }
}
