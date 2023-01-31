package prog;

import java.util.Scanner;

public class Ejercicio13 {

	public static void main(String[] args) {
		int numero=0;
		int cont=0;
		int max=0;
		int min=0;
		
		Scanner sc = new Scanner(System.in);
		
		while(cont<=10){
			System.out.print("Introduce un numero: ");
			numero=Integer.valueOf(sc.nextLine());
			
			if(cont==1) {
				max=numero;
				min=numero;
				cont++;
			}else {
				if(numero>max) {
					max=numero;
					cont++;
				}else if(numero<min) {
					min=numero;
					cont++;
				}else {
					cont++;
				}	
			}
			
			
			
		}
		System.out.print("Numero maximo: "+max+"\n");
		System.out.print("Numero minimo: "+min);
		
	}

}
