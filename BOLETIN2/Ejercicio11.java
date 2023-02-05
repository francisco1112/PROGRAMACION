package prog2;

public class Ejercicio11 {

	public static void main(String[] args) {
		System.out.println(mcm(24,36));
	}
	public static int gcd(int a, int b) {
		while(b>0) {
			int r=a%b;
			a=b;
			b=r;
		}return a;
	}
	
	public static int mcm(int a, int b) {
		int mcm=(a*b)/gcd(a, b);
			
		return mcm;
}
}
