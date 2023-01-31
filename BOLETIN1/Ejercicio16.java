package prog;

import java.util.Scanner;

public class Ejercicio16 {

	public static void main(String[] args) {
		
		int numero=0; 
		int	cont=0; 
		int	mayor=0; 
		int	suma=0;
		
		Scanner sc = new Scanner(System.in);
		
		while(cont<3) {
			
			System.out.print("Introduce los sueldos de cada empleado: ");
			numero=Integer.valueOf(sc.nextLine());
			
			cont++;
			suma =suma+numero;
			if(numero>=1000) {
				mayor++;
			}
		}
		System.out.println("Suma total es: "+suma);
		System.out.println("Total empleados con mas de 1000€ de sueldo: "+mayor);
		
	}
}

