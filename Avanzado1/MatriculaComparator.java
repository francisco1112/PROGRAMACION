package Avanzado1;

import java.util.Comparator;

public class MatriculaComparator implements Comparator<Vehiculo>{

	@Override
	public int compare(Vehiculo o1, Vehiculo o2) {
		int res=0;
		
		if(o2!=null && o1!=null) {
			res = o1.getMatricula().compareTo(o2.getMatricula());
		}else if(o1==null) {
			res=1;
		}else if(o2==null) {
			res=-1;
		}
		
		return res;
	}

}
