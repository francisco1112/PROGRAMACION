package prog;

import java.util.Scanner;

public class Ejercicio11 {

	public static void main(String[] args) {
		int numero=0;
		System.out.println("Dame un numero: ");
		Scanner sc = new Scanner(System.in);
		String loqueintroduceelusuario=sc.nextLine();
		
		numero=Integer.valueOf(loqueintroduceelusuario);
		
		while(numero>=0) {
			System.out.println("El cuadrado de "+numero+" es "+numero*numero);
			System.out.println("Dame otro numero: ");
			Scanner sc1 = new Scanner(System.in);
			String loqueintroduceelusuario1=sc1.nextLine();
			
			numero=Integer.valueOf(loqueintroduceelusuario1);
		}
		
	}

}
