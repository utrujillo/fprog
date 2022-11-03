class Arreglos {
  public static void main(String args[]){
    // Arreglos el equivalente a tuplas
    Integer numeros[] = {1, 6, 9};

    // Verificar el tipo de dato de la variable
    // .getClass().getSimpleName()
    // System.out.println(numeros[1].getClass().getSimpleName());
    // for( int i = 0; i < numeros.length; i++ ){
    //   System.out.println("Indice: "+ i + " valor: "+ numeros[i]);
    // }

    for(Integer valor : numeros){
      System.out.println(valor);
    }

  }
}