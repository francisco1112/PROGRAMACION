package prog3;

public class Ejercicio1 {

	public static void main(String[] args) {
		System.out.println(imprimirPosicion("par", "cadena"));
	}
	public static String imprimirPosicion(String bandera, String cadena) {
		String mensaje="";
		if (bandera.equals("par")) {
			for(int i=0; i<cadena.length() ; i++) {
				if (i%2==0) {
				mensaje+=cadena.charAt(i);
				}
			}
		}else if (bandera.equals("impar")) {
			for(int i=0; i<cadena.length();i++) {
				if (i%2==1) {
					mensaje+=cadena.charAt(i);
				}
			}
		}else {
			mensaje="ERROR";
		}
		
		return mensaje;
	}
}
