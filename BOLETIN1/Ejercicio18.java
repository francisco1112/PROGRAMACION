package prog;

public class Ejercicio18 {
	public static double calcularAreaCirculo(double pi, double r)
	{
			return pi*(r*r);
	}
	
	public static double calcularLongitudCirculo(double d, double r) {
		
		return r*d; 
	}

	
	public static void main(String[] args) {

		
		System.out.println(calcularAreaCirculo(3.14, 2));
		System.out.println(calcularLongitudCirculo(50, 2));

	}

}
