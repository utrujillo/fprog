import java.util.Scanner;
class EjercicioWhile {
  public static void main(String args[]){

    Boolean respuesta = true;
    Scanner sc = new Scanner(System.in);

    while(respuesta){
		System.out.println("** Fundamentos de programacion **\n"
			+"1.- Alta\n"
			+"2.- Baja"
			);
		System.out.println("Ingresa una opcion...");
		Integer opcion = sc.nextInt();
		String opcionSeleccionada = "";
		switch(opcion){
			case 1: {
				opcionSeleccionada = "Has seleccionado dar de alta";
			} break;
			case 2: {
				opcionSeleccionada = "Dar de baja x cosa";
			} break;
			default:
				opcionSeleccionada = "Opcion no valida";
		}
		System.out.println(opcionSeleccionada);

		System.out.println("Deseas realizar otra accion S/N?");
		sc.nextLine();
		String resp = sc.nextLine();
		respuesta = resp.equals("s") ? true : false;
    }

	System.out.println(respuesta);

  }
}