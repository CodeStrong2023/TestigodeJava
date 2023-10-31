import java.util.Scanner;

public class Clase3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Proporciona el titulo");
        String titulo = scanner.nextLine();
        System.out.println("Proporciona el autor");
        String autor = scanner.nextLine();
        System.out.println(titulo +" fue escrito por " + autor);
}
}
