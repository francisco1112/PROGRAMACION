package prog;

import java.util.Scanner;

public class Ejercicio9 {

	public static void main(String[] args) {
		int numero=0;
		int cont=0;
		boolean multiplo=false;
		
		while(cont<5) {
			System.out.println("Dame un numero: ");
			Scanner sc1 = new Scanner (System.in);
			String loQueIntroduceElUsuario1 = sc1.nextLine();
			
			numero = Integer.valueOf(loQueIntroduceElUsuario1);
			cont++;
			if (numero%3==0){
				multiplo=true;			
			}
			System.out.println("El numero "+numero +" multiplo de 3 es "+ multiplo);
		}
	}

}
