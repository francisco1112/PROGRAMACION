package prog3;

public class Ejercicio7 {

	public static void main(String[] args) {
		System.out.println(encontrarPalabra("shybaoxlna", "hola"));
		System.out.println(encontrarPalabra("soybahxlna", "hoy"));
		System.out.println(encontrarPalabra("ysnxipkrñinwmppa", "niña"));
	}
	public static boolean encontrarPalabra(String cadena, String palabra) {
		boolean mensaje=false;
		String encontrada="";
		int e=0;		
		for (int i=0; i<cadena.length() ; i++) {
				while(cadena.charAt(i)==palabra.charAt(e)) {
					encontrada+=cadena.charAt(i);
					if (palabra.equals(encontrada)) {
						e=0;
					}				
					e++;					
				}			
		}
		if (palabra.equals(encontrada)) {
			mensaje=true;
		}		
		return mensaje;
	}
}
