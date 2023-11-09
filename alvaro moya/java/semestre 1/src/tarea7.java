
public class tarea7 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int Horas;
        double Sueldo;
        String Nombre;
        double Salario; 
        System.out.println("Nombre del empleado: ");
        Nombre=teclado.nextLine();
        System.out.println("Horas trabajadas en la semana: ");
        Horas=teclado.nextInt();
        System.out.println("Salario por hora: ");
        Sueldo=teclado.nextDouble();
        Salario=Sueldo * Horas;
        System.out.println("El empleado"+Nombre+"cobra un salario de $"+Salario);
        
    }
}
