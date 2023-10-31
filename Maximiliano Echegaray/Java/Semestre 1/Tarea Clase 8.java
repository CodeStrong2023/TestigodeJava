import java.util.Scanner;

public class Clase8 {
    public static void main(String[] args) {
        //Ejercicio Area del Rectangulo//
        Scanner teclado = new Scanner (System.in);
     /*   int Alto;
        int Ancho;
        int Area;
        int Perimetro;
        System.out.println("Digite el alto del rectangulo");
        Alto= teclado.nextInt();
        System.out.println("Digite el ancho del rectangulo");
        Ancho= teclado.nextInt();
        Area= Alto * Ancho;
        System.out.println("El area del rectangulo es "+Area);
        Perimetro= (Alto + Ancho) * 2;
        System.out.println("El perimetro del rectangulo es "+Perimetro);
       */
        
        
        int Num1;
        int Num2;
        int Mayor;
        System.out.println("Digite el numero 1");
        Num1 = teclado.nextInt();
        System.out.println("Digite el numero 2");
        Num2 = teclado.nextInt();
        Mayor=(Num1>Num2)?Num1:Num2;
        System.out.println("El numero mayor es "+Mayor);
    }
}
