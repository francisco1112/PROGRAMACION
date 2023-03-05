package OriObj2;

public class PartidoPrincipal {

	public static void main(String[] args) {
		Equipo lora = new Equipo("Lora", "Nuestra Señora De Setefilla", "Lora del rio");
		
		Equipo brenes = new Equipo("Brenes", "Estadio Municipal De San Sebastian", "Brenes");
		
		Partido jornada1 = new Partido(lora, brenes, 1);
		
		System.out.println(jornada1);
		
		jornada1.ponerResultado(jornada1, "2-1");
		
		System.out.println(jornada1);
		
		jornada1.ponerResultado(jornada1, "1-2");
		
		System.out.println(jornada1);
		
		jornada1.ponerResultado(jornada1, "0-0");
		
		System.out.println(jornada1);
		
		jornada1.ponerResultado(jornada1, "");
		
		System.out.println(jornada1);
		
		jornada1.ponerResultado(jornada1, "A-0");
		
		System.out.println(jornada1);

	}

}
