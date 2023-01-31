package prog;

public class Ejercicio7 {

	public static final int LOWER_LIMIT=0;
	public static final int UPPER_LIMIT=100;
	
	public static final int LOWER_LIMIT180=180;
	public static final int UPPER_LIMIT340=340;


	public static void main(String[] args) {
		int i=1;
		
		System.out.println("a)while");

		while(i<=UPPER_LIMIT) {
			System.out.println(i);
			i++;
		}
		
		System.out.println("a)for");

		for(i=1; i<=UPPER_LIMIT;i++) {
			System.out.println(i);
		}
		
		System.out.println("a)do_while");
		i=LOWER_LIMIT;
		
		do {i++;System.out.println(i);
		}while (i<UPPER_LIMIT);
		
		System.out.println("b)while");
		i=UPPER_LIMIT;

		while(i>=1) {
			System.out.println(i);
			i--;
		}
		
		System.out.println("b)for");

		for(i=UPPER_LIMIT; i>=1;i--) {
			System.out.println(i);
		}
		
		System.out.println("b)do_while");
		
		i=UPPER_LIMIT;
		
		do {i--;System.out.println(i);
		}while (i>1);
		
		System.out.println("c)while");
		i=LOWER_LIMIT;

		while(i<=20) {
			System.out.println(i*5);
			i++;
		}
		
		System.out.println("c)for");

		for(i=LOWER_LIMIT; i<=20;i++) {
			System.out.println(i*5);
		}
		
		System.out.println("c)do_while");
		
		i=LOWER_LIMIT;
		
		do {i++;System.out.println(i*5);
		}while (i<20);
		
		System.out.println("d)while");
		
		i=UPPER_LIMIT340;
		int resto=LOWER_LIMIT;
		

		while(i>=LOWER_LIMIT180) {
			i=i-20;
			System.out.println(i);
		}
		
		System.out.println("d)for");
		
		for (i=UPPER_LIMIT340;i>=LOWER_LIMIT180;i=i-20) {
			System.out.println(i);
		}
		i=UPPER_LIMIT340;
		
		do {i=i-20;System.out.println(i);
		}while (i>160);
	}

}
