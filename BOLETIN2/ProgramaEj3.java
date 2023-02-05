package prog2;

public class ProgramaEj3 {

	public static void main(String[] args) {
		Password password = new Password("1234aAb;");
		System.out.println(password.esFuerte());
		
		System.out.println(new Password("1234a;").esFuerte());
		System.out.println(new Password("12").esFuerte());
		System.out.println(new Password("1234a;AA").esFuerte());
	}

}
