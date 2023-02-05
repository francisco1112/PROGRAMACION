package prog2;

import java.util.Scanner;

public class Ejercicio8 {

	public static void main(String[] args) {
		int numero =0 ;
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Introduce el numero para convertir a binario: ");
		numero = Integer.valueOf(sc.nextLine());
		
		System.out.println(toBinary(numero));
	}
	
	public static String toBinary(int decimal) {
		String binario ="";
		while(decimal>=2) {
			int resto=decimal%2;
			binario=resto+binario;
			decimal=decimal/2;
		}
		return decimal+binario;
	}

}
