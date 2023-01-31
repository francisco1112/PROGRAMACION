package prog;

import java.util.Scanner;

public class Ejercicio10 {

	public static void main(String[] args) {
		int numero=0;
		int cont=0;
		int total=0;
		System.out.println("Dame un numero: ");
		Scanner sc = new Scanner (System.in);
		String loqueelusuariomete=sc.nextLine();
		cont=Integer.valueOf(loqueelusuariomete);

		
		
		
		
			if(cont>=0) {
				while(cont<=100) {
					total+=cont;
					cont++;
				}
				System.out.println("El total es: "+total);
			
			}else {
				System.out.println("El numero no es valido.");
			}
		
	}

}
