package prog;

import java.util.Scanner;

public class Ejercicio5 {

	public static void main(String[] args) {
		int hora=0;
		System.out.println("¿Qué hora es?");
		Scanner sc3 = new Scanner (System.in);
		String loQueIntroduceElUsuario1 = sc3.nextLine();
		hora = Integer.valueOf(loQueIntroduceElUsuario1);
		
		if (hora>=6 && hora<=12) {
			System.out.println("Buenos días.");
		}else if(hora>=13 && hora<=20) {
			System.out.println("Buenos tardes.");
		}else if (hora>=21 && hora<=23 || hora>=0 && hora<=5) {
			System.out.println("Buenas noches.");
		}
	}

}
