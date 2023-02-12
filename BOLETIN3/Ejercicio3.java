package prog3;

public class Ejercicio3 {

	public static void main(String[] args) {
		System.out.println(contarPalabras("cadena CA CA CA", "CA"));
	}
	public static int contarPalabras(String cadena, String palabra) {
		int mensaje=0;
		int i=0;
		if (cadena!=null || !cadena.isEmpty()) {
			do {
				if (cadena.contains(palabra)) {
				mensaje++;
				
				cadena=cadena.substring(cadena.indexOf(palabra)+palabra.length());
				}
				i++;
			}while(i<cadena.length());
		}
		
		
		return mensaje;
	}
}
