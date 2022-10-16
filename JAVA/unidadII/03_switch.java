// Los dias Sabado y Domingo:
// - Es fin de semana, no trabajar
// Los dias pares regresar: martes y jueves
// - Hacer tareas
// Los dias impares regresar: los demas
// - Date tiempo para ir al parque a pasear
import java.util.Scanner;

class EjercicioSwitch {
  public static void main(String args[]){
    /*
      Sintaxis - Switch
      switch( condicion ){
        case valor: { codigo a ejecutar } break;
        default: { ... }
      }
    */
    System.out.println("Escribe el dia de la semana:");
    Scanner sc = new Scanner(System.in);
    String dia = sc.nextLine();

    switch(dia){
      case "lunes": case "miercoles": case "viernes": {
        System.out.println("Date tiempo para ir al parque a pasear");
      } break;
      case "martes": case "jueves": {
        System.out.println("Hacer tareas");
      } break;
      default: {
        System.out.println("Es fin de semana, no trabajar");
      }
    }
  }
}