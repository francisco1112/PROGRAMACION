package prog;

import java.util.Scanner;

public class Ejercicio3 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		char caracter = scanner.nextLine().charAt(0);
		
		System.out.println(caracter);
				
		
		if (Character.isUpperCase(caracter)) {
			System.out.println("Letra may�scula.");
		}else if(Character.isLowerCase(caracter)) {
			System.out.println("Letra min�scula.");
		}else if(Character.isDigit(caracter)) {
			System.out.println("Digito entre 0 y 9.");
		}else if(caracter == '(' || caracter == ')' || caracter == '{' || caracter == '}') {
			System.out.println("Par�ntesis o llaves.");
		}else if(caracter == ' ' ) {
			System.out.println("Espacio en blanco.");
		}else {
			System.out.println("Otro caracter.");
		}
		/*
		
		switch(caracter) {
		case '.',';',':','!','�','?','�','+','*','-','/' :{
				System.out.println("Signo de puntuaci�n.");
				break;
			}
		case Character.isLowerCase(caracter):{
			System.out.println("Letra min�scula.");
			break;
		}
		case Character.isUpperCase(caracter):{
			System.out.println("Letra may�scula.");
			break;
		}
		case '(',')','{','}':{
			System.out.println("Par�ntesis o llaves.");
			break;
		}
		case ' ':{
			System.out.println("Espacio en blanco.");
			break;
		}
		case '0','1','2','3','4','5','6','7','8','9':{
			System.out.println("Digito entre 0 y 9.");
			break;
		}
		default: {
			System.out.println("Otro caracter.");
		}
	
	}
	*/
	}

}
