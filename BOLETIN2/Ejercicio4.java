package prog2;

import java.util.Scanner;

public class Ejercicio4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("introduce un frase: ");
		String cadena = sc.nextLine();
		String invertida = "";
		int i = 1;
		while(i <cadena.length()) {
			System.out.print(cadena.charAt(i));
			System.out.print(cadena.charAt(i-1));
			i+=2;	
			}
		if (cadena.length()%2==1) {
			System.out.print(cadena.charAt(cadena.length()-1));
			}
	}

}
