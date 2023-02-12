package prog3;

public class Ejercicio5 {

	public static void main(String[] args) {
		System.out.println(esPalindromo("cadena"));
	}
		public static boolean esPalindromo(String cadena) {
			boolean mensaje=true;
			if (!cadena.isEmpty() && cadena!=null) {		
				for (int j=0; j<cadena.replace(" ", "").length() ; j++) {
					if (cadena.replace(" ", "").charAt(j)!=cadena.replace(" ", "").charAt(cadena.replace(" ", "").length()-1-j)) {
						mensaje=false;
					}			
				}		
			}		
			return mensaje;
		}

}
