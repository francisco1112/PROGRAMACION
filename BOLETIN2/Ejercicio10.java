package prog2;

public class Ejercicio10 {

	public static void main(String[] args) {
		System.out.println(gcd(120, 56));
		System.out.println(gcd(24, 3));
	}
	public static int gcd(int a, int b) {
		while(b>0) {
			int r=a%b;
			a=b;
			b=r;
		}
		
		
		return a;
}
}
