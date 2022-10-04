import java.util.Scanner;

class EntradaDatos {
  public static void main(String args[]){
    // System.out.println("Ingresa un saludo: ");

    // Scanner entrada = new Scanner(System.in);
    // String saludo = entrada.nextLine();

    // System.out.println("Tu saludo es: "+ saludo);
    System.out.println("Ingresa un numero");
    Scanner entrada = new Scanner(System.in);
    Integer numero = entrada.nextInt();
    System.out.println("Tu numero es: "+ numero);
  }
}