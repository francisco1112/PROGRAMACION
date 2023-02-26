package OriObj;

import java.util.Scanner;

public class RectanguloPrincipal {

	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		
		Rectangulo rectangulo;
		
		double ancho=0;
		double longitud=0;
		
		System.out.println("Longitud del rectangulo: ");
		longitud=Double.valueOf(sc.nextLine());
		
		System.out.println("Ancho del rectangulo: ");
		ancho=Double.valueOf(sc.nextLine());
		
		rectangulo = new Rectangulo(longitud, ancho);
		
		System.out.println(rectangulo);
	}

}
