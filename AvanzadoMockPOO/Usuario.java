package AvanzadoMockPOO;

import java.util.Objects;

public class Usuario {
	private String login;
	private String pass;
	
	public Usuario(String login, String pass) {
		super();
		this.login = login;
		this.pass = pass;
	}
	
	
	
	//getters y setters

	public String getLogin() {
		return login;
	}

	public boolean setPass(String pass, String newPass) {
		boolean res = false;
		
		if(pass!=null && !pass.isEmpty() && this.pass.equals(pass)) {
			this.pass=newPass;
			res=true;
		}
		
		
		return res;
	}
	
	public boolean checkPass(String pass) {
		return pass!=null && !pass.isEmpty() && this.pass.equals(pass)?true:false;
	}



	@Override
	public int hashCode() {
		return Objects.hash(login, pass);
	}



	@Override
	public boolean equals(Object obj) {
		boolean sonIguales=this==obj;
		
		if(!sonIguales && obj!=null && obj instanceof Usuario) {
			Usuario otroUsuario=(Usuario) obj;
			sonIguales = this.login!=null && !this.login.isEmpty() && otroUsuario.login!=null && !otroUsuario.login.isEmpty() 
					&& this.login.equals(otroUsuario.login); 
		}
		
		return sonIguales;
	}
	
	
	
	
	

	
	
}
