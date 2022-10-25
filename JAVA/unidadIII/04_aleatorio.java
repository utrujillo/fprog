import java.util.Random;

class Aleatorio {
  public static void main(String args[]){
    Random random = new Random();
    Integer numberRandom = random.nextInt(50 - 0) + 0;
    // System.out.println( numberRandom );
    // a - 97 hasta z - 122
    char letterRandom = (char) (random.nextInt(122 - 97) + 97);
    // System.out.println( letterRandom );

    String cadena = "La Kymberly y el Bryannnnnnn";
    System.out.println("Mayusculas: "+ cadena.toUpperCase());
    System.out.println("Minusculas: "+ cadena.toLowerCase());
    System.out.println("Capitalize: "+ 
      cadena.substring(0,1).toUpperCase() 
      + cadena.substring(1).toLowerCase()
      );
    System.out.println("Reemplazar: y por yyy "+ cadena.replace("y", "yyy"));
    for( char letra: cadena.toCharArray() ) {
      System.out.println( letra );
    }
  }
}