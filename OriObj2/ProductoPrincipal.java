package OriObj2;

public class ProductoPrincipal {

	public static void main(String[] args) {
		Producto uno = new Producto("azul", 10);
		Producto dos = new Producto("verde", 11);
		
		System.out.println(uno.hashCode());
		System.out.println(dos.hashCode());
		
		System.out.println(uno.calcularPrecioIVA());
	}

}
