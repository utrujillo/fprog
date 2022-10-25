class Ejercicio {
  public static void main(String args[]){
    Integer a_fin = 2018;
    for( Integer a_inicio = 2015; a_inicio <= a_fin; a_inicio++ ){
      // System.out.println(a_inicio);
      Integer m_fin = 12;
      for ( Integer m_inicio = 1; m_inicio <= m_fin; m_inicio++  ){
        System.out.println( a_inicio +"     "+ m_inicio +"      monto" );
      }
    }
  }
}