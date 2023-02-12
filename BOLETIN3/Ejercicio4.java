package prog3;

public class Ejercicio4 {

	public static void main(String[] args) {
		System.out.println(empiezaPor("mi amigo entra por la puerta", "mi"));
		System.out.println(empiezaPor("mi amigo entra por la puerta", "por"));
		System.out.println(terminaPor("mi amigo entra por la puerta", "puerta"));
		System.out.println(terminaPor("mi amigo entra por la puerta", "por"));
		System.out.println(contiene("mi amigo entra por la puerta", "entra"));
		System.out.println(contiene("mi amigo entra por la puerta", "la"));


	}
	public static boolean empiezaPor(String frase, String palabra) {
		boolean mensaje = false;
		if (frase.indexOf(palabra)==0) {
			mensaje=true;
		}
		return mensaje;
	}
	
	
	public static boolean contiene(String frase, String palabra) {
		boolean mensaje = false;
		for(int i=0; i<frase.length(); i++) {
			if (frase.indexOf(palabra)==i) {
				mensaje = true;
			}
		}
		
		return mensaje;
}
	public static boolean terminaPor(String frase, String palabra) {
		boolean mensaje = false;
		if (frase.indexOf(palabra)==(frase.length())-palabra.length()) {
			mensaje=true;
		}
		return mensaje;
	}
}