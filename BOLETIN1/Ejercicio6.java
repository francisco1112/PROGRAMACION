package prog;

import java.util.Scanner;

public class Ejercicio6 {

	public static void main(String[] args) {
		int dia=0;
		System.out.println("�En qu� dia estas?");
		Scanner sc3 = new Scanner (System.in);
		String loQueIntroduceElUsuario1 = sc3.nextLine();
		dia = Integer.valueOf(loQueIntroduceElUsuario1);
		
		int mes=0;
		System.out.println("�En qu� mes estas?");
		Scanner sc4 = new Scanner (System.in);
		String loQueIntroduceElUsuario2 = sc4.nextLine();
		mes = Integer.valueOf(loQueIntroduceElUsuario2);
		
		if (dia>=20 && mes>=3 && mes<=6) {
			System.out.println("20�C");
		}else if(dia>=21 && mes>=6 && mes<=9 ) {
			System.out.println("24�");
		}else if (dia>=23 && mes>=9 && mes<=12) {
			System.out.println("24�C");
		}
	}

}
