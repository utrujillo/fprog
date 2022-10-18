import java.util.Scanner;
class HolaMundo {
  public static void main(String args[]){
    System.out.println("Ingresa un texto: ");
    Scanner sc = new Scanner(System.in);
    String cadena = sc.nextLine();
    System.out.println("En mayuscula: "+ cadena.toUpperCase());
    System.out.println("En minuscula: "+ cadena.toLowerCase());
    // for( inicio; condicion; incremento ){}
    // for( Integer inicio = 1; inicio <= 10; inicio++ ){
    //   System.out.println("Numero "+ inicio);
    // }
  }
}