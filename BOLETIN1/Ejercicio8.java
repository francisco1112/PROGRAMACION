package prog;

import java.util.Scanner;

public class Ejercicio8 {

	public static void main(String[] args) {
		int numero=0;
		int cont=0;
		int suma=0;
		
		while(cont<15) {
			System.out.println("Dame un numero: ");
			Scanner sc1 = new Scanner (System.in);
			String loQueIntroduceElUsuario1 = sc1.nextLine();
			
			numero = Integer.valueOf(loQueIntroduceElUsuario1);
			cont++;
			suma+=numero;
		}
		System.out.println("La suma de todos los numeros es: "+suma);
		
		
	}

}
