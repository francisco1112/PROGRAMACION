package AvanzadoMockPOO;

import java.time.LocalDateTime;
import java.util.Objects;

public abstract class Publicacion {
	
	protected String texto;
	private LocalDateTime fechaCreacion;
	protected int valoracion;
	private int codigo;
	private static int codigoSiguiente;
	private Usuario usuario;
	
	public Publicacion(String texto, Usuario usuario) {
		super();
		this.texto = texto;
		this.usuario = usuario;
		this.fechaCreacion=LocalDateTime.now();
		this.codigo=codigoSiguiente++;
	}
	
	
	
	
	
	protected abstract void setTexto(String texto) throws PublicacionException;

	@Override
	public int hashCode() {
		return Objects.hash(usuario, fechaCreacion);
	}


	@Override
	public boolean equals(Object obj) {
		boolean sonIguales = this == obj;
		
		if(!sonIguales && obj!=null && obj instanceof Publicacion) {
			Publicacion otraPublicacion=(Publicacion)obj;
			
			sonIguales = this.codigo == otraPublicacion.codigo;
		}
		
		return sonIguales;
	}

	public boolean valorar(String valoracion) {
		
		Valoraciones v= Valoraciones.valueOf(valoracion.toUpperCase());
		this.valoracion=+v.getValoracion();
		
		return true;
	}
	
	public String getLoginUsuario() {
		return this.usuario.getLogin();
	}
	
	


	//toString
	@Override
	public String toString() {
		return "Publicacion [texto=" + texto + ", fechaCreacion=" + fechaCreacion + ", valoracion=" + valoracion
				+ ", codigo=" + codigo + "]";
	}

	public int compareTo(Publicacion o) {
		return this.fechaCreacion.compareTo(o.fechaCreacion);
	}
	
	public boolean isAnterior(Publicacion o) {
		return this.fechaCreacion.isBefore(o.fechaCreacion);
	}


	//getters y setters
	public String getTexto() {
		return texto;
	}


	public LocalDateTime getFechaCreacion() {
		return fechaCreacion;
	}

	public int getValoracion() {
		return valoracion;
	}

	public int getCodigo() {
		return codigo;
	}
	
	
	
	
}
