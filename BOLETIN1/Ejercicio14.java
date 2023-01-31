package prog;

import java.util.Scanner;

public class Ejercicio14 {

	public static void main(String[] args) {
		int numero=0;
		int cont=0;
		int par=0;
		int totalimpar=0;
		int mediaimpar=0;
		int contimpar=0;
		
		System.out.println("Introduce un numero: ");
		Scanner sc = new Scanner (System.in);
		String loqueintroduceelusuario = sc.nextLine();
		numero=Integer.valueOf(loqueintroduceelusuario);
		
		while (numero>=0) {
			if (numero%2==0){
				if (numero>=par) {
					par=numero;
				}
			}else if(numero%1==0) {
					totalimpar+=numero;
					contimpar++;
					
			}
			System.out.println("Introduce otro numero: ");
			Scanner sc1 = new Scanner (System.in);
			String loqueintroduceelusuario1 = sc1.nextLine();
			numero=Integer.valueOf(loqueintroduceelusuario1);
			
			cont++;
		}
		System.out.println("Se han introducido "+cont+" numeros");
		
		System.out.println("El mayor numero par es "+par);
		System.out.println("La media de los impares es "+totalimpar/contimpar);
	}

}
