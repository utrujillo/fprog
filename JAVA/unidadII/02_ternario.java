class HolaMundo {
  public static void main(String args[]){
    /*
      Sintaxis
      ( condicion ) ? true : false ;
    */
    Boolean ticket = true;
    String mensaje = (ticket) ? "No cobrar" : "Cobrar";
    System.out.println( mensaje );
    // if( ticket ){
    //   System.out.println("No cobrar");
    // }else{
    //   System.out.println("Cobrar");
    // }
  }
}