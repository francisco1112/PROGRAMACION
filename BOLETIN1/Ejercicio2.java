package prog;

import java.util.Scanner;

public class Ejercicio2 {

	public static void main(String[] args) {
		System.out.println("Dia de la semana: ");
		String dia = new Scanner(System.in).nextLine();
		
		switch (dia) {
		case "Lunes" :{
			System.out.println("Entorno de Desarrollo");	
			break;
		}case "Martes":{
			System.out.println("FOL");	
			break;
		}case "Miercoles", "Viernes":{
			System.out.println("Sistemas Informaticos");
			break;
		}case "Jueves":{
			System.out.println("Base de Datos");
			break;
		}default:{
			System.out.println("El dia introducido es erróneo");
			}
		}
	}

}
