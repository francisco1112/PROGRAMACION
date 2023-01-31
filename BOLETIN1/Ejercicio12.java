package prog;

import java.util.Scanner;

public class Ejercicio12 {

	public static void main(String[] args) {
		int numero=0;
		int cont=1;
		
		System.out.println("Dame un numero: ");
		Scanner sc = new Scanner(System.in);
		String loqueintroduceusuario=sc.nextLine();
		
		numero=Integer.valueOf(loqueintroduceusuario);
		
		while(numero>=0) {
			System.out.println("Dame otro numero: ");
			Scanner sc1 = new Scanner(System.in);
			String loqueintroduceusuario1=sc1.nextLine();
			
			numero=Integer.valueOf(loqueintroduceusuario1);
			cont++;
		}
		System.out.println("Se han introducido "+ cont +" numeros");
	}

}
