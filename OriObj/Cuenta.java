package OriObj;

public class Cuenta {
	private double saldo;
	private int numeroIngresos;
	private int numeroReintegros;
	
	public void CuentaCorriente() {
		this.saldo 				= 0;
		this.numeroIngresos 	= 0;
		this.numeroReintegros 	= 0;
	}
	
	
	public boolean retirar(double cantidadRetirar) {
		boolean ingresoRealizado=false;
		
		if(cantidadRetirar > 0 && this.saldo>=cantidadRetirar) {
			this.saldo-=cantidadRetirar;
			this.numeroIngresos++;
			ingresoRealizado=true;
		}
		return ingresoRealizado;
	}
	
	public boolean ingresar(double cantidadIngresar) {
		boolean ingresoRealizado=false;
		
		if(cantidadIngresar > 0) {
			this.saldo+=cantidadIngresar;
			this.numeroIngresos++;
			ingresoRealizado=true;
		}
		return ingresoRealizado;
	}
	
	

	public double getSaldo() {
		return saldo;
	}


	@Override
	public String toString() {
		return "La CuentaCorriente tiene un saldo de " + saldo + ", con numero de Ingresos " + numeroIngresos + " y numero de Reintegros "
				+ numeroReintegros;
	}
}
