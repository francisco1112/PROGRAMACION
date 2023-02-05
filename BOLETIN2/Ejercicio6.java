package prog2;

import java.util.Scanner;

public class Ejercicio6 {

	public static void main(String[] args) {
		
		int h1=0;
		int m1=0;
		int s1=0;
		int h2=0;
		int m2=0;
		int s2=0;

		
		
		System.out.println("Horas1: ");
		Scanner sc1 = new Scanner (System.in);
		String loQueIntroduceElUsuario1 = sc1.nextLine();
		
		h1 = Integer.valueOf(loQueIntroduceElUsuario1);
		
		System.out.println("Minutos1: ");
		Scanner sc2 = new Scanner (System.in);
		String loQueIntroduceElUsuario2 = sc2.nextLine();
		
		m1 = Integer.valueOf(loQueIntroduceElUsuario2);
		
		
		System.out.println("Segundos1: ");
		Scanner sc3 = new Scanner (System.in);
		String loQueIntroduceElUsuario3 = sc3.nextLine();
		
		s1 = Integer.valueOf(loQueIntroduceElUsuario3);
		
		System.out.println("Horas2: ");
		Scanner sc4 = new Scanner (System.in);
		String loQueIntroduceElUsuario4 = sc4.nextLine();
		
		h2 = Integer.valueOf(loQueIntroduceElUsuario4);
		
		
		System.out.println("Minutos2: ");
		Scanner sc5 = new Scanner (System.in);
		String loQueIntroduceElUsuario5 = sc5.nextLine();
		
		m2 = Integer.valueOf(loQueIntroduceElUsuario5);
		
		System.out.println("Segundos2: ");
		Scanner sc6 = new Scanner (System.in);
		String loQueIntroduceElUsuario6 = sc6.nextLine();
		
		s2 = Integer.valueOf(loQueIntroduceElUsuario6);
		
		System.out.println(horaMayor(h1,m1,s1,h2,m1,s2));
	}
	public static int horaMayor(int h1, int m1, int s1, int h2, int m2, int s2) {
		int mayor=0;
		while(h1<=23 && h1>=0 && h2<=23 && h2>=0 && m1>=0 && m1<=59&& m2>=0 && m2<=59 && s1>=0 && s1<=59&& s2>=0 && s2<=59) {
			if ((h1>h2)||(h1==h2 && m1>m2) || (h1==h2 && m1==m2 && s1>s2))  {
				mayor=1;
			}else if((h2>h1)||(h1==h2 && m2>m1) || (h1==h2 && m1==m2 && s2>s1)) {
				mayor=2;
			}else if(h1==h2 && m1==m2 && s1==s2) {
				mayor=0;
			}
		}
		mayor=-1000;
		
		return mayor;
	}

}
