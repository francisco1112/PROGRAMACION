package prog2;

import java.util.Scanner;

public class Ejercicio5 {
	public static void main(String[] args){
	int numero1=0;
	int numero2=0;
	
	System.out.println("Dame un numero: ");
	Scanner sc1 = new Scanner (System.in);
	String loQueIntroduceElUsuario1 = sc1.nextLine();
	
	numero1 = Integer.valueOf(loQueIntroduceElUsuario1);
	
	System.out.println("Dame un numero: ");
	Scanner sc2 = new Scanner (System.in);
	String loQueIntroduceElUsuario = sc2.nextLine();
	
	numero2 = Integer.valueOf(loQueIntroduceElUsuario);
	
	System.out.println(esMultiplo(numero1,numero2));
	}
	
	
	public static boolean esMultiplo(int numero1, int numero2) {
		boolean multiplo=false;		
		if (numero1%numero2==0) {
			multiplo=true;
			}
		return multiplo;
		
		
	}
	

}
