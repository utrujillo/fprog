
import java.util.ArrayList;
import java.util.List;
class Moda {
  public static void main(String args[]){
    // Cambiar el arreglo valores, para verificar diferentes resultados
    List<Integer> moda = new ArrayList<Integer>();
    
    // Verificar el numero maximo de repeticiones que existen
    Integer valores[] = {2, 2, 2, 4, 4, 2, 2, 3, 3, 4, 4, 4, 3, 3, 3 };
    Integer maxRepetitions = 0;
    for( int i = 0; i < valores.length; i++ ){
      Integer fileRepetitions = 0;
      for( int j = 0; j < valores.length; j++ ){
        if ( valores[i] == valores[j] ){
          fileRepetitions += 1;
        }
      }
      if( fileRepetitions > maxRepetitions )
        maxRepetitions = fileRepetitions;
    }
    System.out.println("Max Repetitions "+ maxRepetitions);
    
    // Obtiene la moda
    for( int i = 0; i < valores.length; i++ ){
      Integer fileRepetitions = 0;
      for( int j = 0; j < valores.length; j++ ){
        if ( valores[i] == valores[j] ){
          fileRepetitions += 1;
        }
      }

      if( fileRepetitions == maxRepetitions && !moda.contains(valores[i]) ){
        moda.add( valores[i] );
      }
    }

    System.out.println( moda );
  }
}