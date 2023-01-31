package prog;

import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		int numero1=0;
		int numero2=0;
		boolean respuesta=false;
		
		System.out.println("¿Cual es el número1?: ");
		Scanner sc = new Scanner (System.in);
		String loQueIntroduceElUsuario = sc.nextLine();
		
		numero1 = Integer.valueOf(loQueIntroduceElUsuario);
		
		System.out.println("¿Cual es el número2?: ");
		Scanner sc1 = new Scanner (System.in);
		String loQueIntroduceElUsuario1 = sc1.nextLine();
		
		numero2 = Integer.valueOf(loQueIntroduceElUsuario1);
		
		if (numero1%numero2==0 || numero2%numero1==0) {
			System.out.println(respuesta=true);
		}else {
			System.out.println(respuesta=false);
		}
	}

}
