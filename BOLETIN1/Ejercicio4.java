package prog;

import java.util.Scanner;

public class Ejercicio4 {

	public static void main(String[] args) {
		double nota_practica=0;
		double nota_problemas=0;
		double nota_teorica=0;

		
		System.out.println("¿Qué nota has sacado en la practica?");
		Scanner sc3 = new Scanner (System.in);
		String loQueIntroduceElUsuario1 = sc3.nextLine();
		nota_practica = Integer.valueOf(loQueIntroduceElUsuario1);
		
		System.out.println("¿Qué nota has saco en problemas?");
		Scanner sc4 = new Scanner (System.in);
		String loQueIntroduceElUsuario2 = sc4.nextLine();
		nota_problemas = Integer.valueOf(loQueIntroduceElUsuario2);
		
		System.out.println("¿Qué nota has sacado en la parte teorica?");
		Scanner sc5 = new Scanner (System.in);
		String loQueIntroduceElUsuario3 = sc5.nextLine();
		nota_teorica = Integer.valueOf(loQueIntroduceElUsuario3);
		
		if (nota_practica>=0 && nota_practica<=10 && nota_problemas<=10 && nota_problemas>=0 && nota_teorica<=10 && nota_teorica>=0) {
			System.out.println("La nota de la practica es: "+100/nota_practica*10);
			System.out.println("La nota de problemas es: "+100/nota_problemas*50);
			System.out.println("La nota de la teoria es: "+100/nota_teorica*40);

		}else {
			System.out.println("ERROR al introducir la nota.");
		}
	}

}
