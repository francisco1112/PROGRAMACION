package prog3;

public class Ejercicio2 {

	public static void main(String[] args) {
		System.out.println(esDivisiblePor3("156"));
		System.out.println(esDivisiblePor3("157"));
		System.out.println(esDivisiblePor3("158"));
	}
		
	public static boolean esDigito(String numero) {
		boolean mensaje = true;
		for(int i=0; i<numero.length() ; i++) {
			if (!Character.isDigit(numero.charAt(i))) {
				mensaje=false;
			}
		}
		
		return mensaje;
	}

	public static boolean esDivisiblePor3(String numero) {
		boolean mensaje = false;
		int suma=0;
		if (esDigito(numero) && numero!=null && !numero.isEmpty()) {
			do {
				for(int i=0; i<numero.length(); i++) {
					suma+=Character.getNumericValue(numero.charAt(i));				
				}
				numero=String.valueOf(suma);
				suma=0;
			}while(Integer.valueOf(numero)>9);
			
			
		}
		if (Integer.valueOf(numero)%3==0) {
			mensaje = true;
		}
		
		return mensaje;
}
}
