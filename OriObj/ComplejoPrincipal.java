package OriObj;

public class ComplejoPrincipal {

	public static void main(String[] args) {
		Complejo a = new Complejo(2.20, 4);
		Complejo b = new Complejo(2.20, 2);
		
		System.out.println(a.suma(b));
		System.out.println(b.resta(a));
		System.out.println(b.equals(a));
	}

}
