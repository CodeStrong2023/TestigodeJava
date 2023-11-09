
import java.lang.NumberFormatException;
import javax.swing.JOptionPane;


public class proyecto {
	

	public static void main(String args[]) {
		String nomus;
		JOptionPane.showMessageDialog(null, "......................:::Arranca con Fuerza:::........................");
		nomus = JOptionPane.showInputDialog("Escriba su nombre: ");
                JOptionPane.showMessageDialog(null, "Bienvenido "+nomus);
		System.out.print(" ");
	
		menu();
	}

	// menu interactivo
	public static void menu() {
		int elemenu;
		// grafica de pago
                try{
                elemenu = Integer.parseInt(JOptionPane.showInputDialog(
                "MENU\n"
               +"1. Planes de Pago\n"
               +"2. Elegir Turno\n"
               +"3. Rutina a entrenar\n"
               +"4. Contador de series en el ejercicio\n"
               +"5. Salir"));
                switch (elemenu) {
		case 1 -> planesdepago();
		case 2 -> turno();
		case 3 -> rut();
		case 4 -> cont();
		case 5 -> JOptionPane.showMessageDialog(null, "Gracias por venir pura sangre!");
		default -> {
                    JOptionPane.showMessageDialog(null, "La opcion elegida es incorrecta,vuelva a seleccionar otra");
                    menu();
                }
		}
                }catch(NumberFormatException ex){
                    JOptionPane.showMessageDialog(null, "La opcion elegida es incorrecta,vuelva a ingresar un numero valido");
                    menu();
                }
	}

	public static void planesdepago() {
		int vol;
		
		JOptionPane.showMessageDialog(null, 
                        "                                                     Planes del Gym\n"
		 +"Dias disponibles    | Lunes |"+"| Martes |"+"| Miercoles |"+"| Jueves |"+"| Viernes |"+"| Sabado |"+"| Domingo |\n"
		 +"1 vez x semana                                  $400\n"
		 +"2 veces x semana                             $2000\n"
		 +"3 veces x semana                             $3000\n"
		 +"6 veces x semana                             $5000\n"
		 +"¿Desea volver al menu?");
		 try{		
                     vol = Integer.parseInt(JOptionPane.showInputDialog(
                        "1. Si desea volver\n"
                       +"2. Si desea salir"));
		// EXPRESIÓN 
		switch (vol) {
		case 1 -> menu();
		case 2 -> JOptionPane.showMessageDialog(null, "Gracias por venir pura sangre".toUpperCase());
		default -> {
                  
                    JOptionPane.showMessageDialog(null,"La opcion es incorrecta, vuelve a elegir otra opcion".toUpperCase());
                planesdepago();    
                }
		}
                 
                 }catch(NumberFormatException ex){
                    JOptionPane.showMessageDialog(null, "La opcion elegida es incorrecta,vuelva a ingresar un numero valido");
                    planesdepago();
                }
		
	}

	public static void turno() {
		int i;
		String nomusu;
		int precios[];
		// iterador que recorre los precios en el arreglo
		// arreglo con los precios de los dintintos planes de rutina 
		precios = new int[4];
		precios[0] = 400;
		precios[1] = 2000;
		precios[2] = 3000;
		precios[3] = 5000;
		
		nomusu = JOptionPane.showInputDialog("¿Nombre del que solicita el turno?: ");
		JOptionPane.showMessageDialog(null, 
                 "1. 1 dias a la semana son $400\n"
		+"2. 2 dias a la semana son $2000\n"
		+"3. 3 dias a la semana son $3000\n"
		+"4. 6 dias a la semana son $5000");
		//i = 0;
                try{
                i = Integer.parseInt(JOptionPane.showInputDialog("¿Cuantos dias va a asistir?"));
                switch (i) {
		case 1 ->
                {
                    JOptionPane.showMessageDialog(null,
                         " ________________________________\n"
			+"| Nombre del usuario: "+nomusu
			+"\n|--------------------------------|"
			+"\n| Dias: 1                          "
                                
                                
			+"\n|--------------------------------|"
			+"\n|Precio:$ "+precios[0]
			+"\n| --------------------------------");
                } 
		case 2 ->
                {
                JOptionPane.showMessageDialog(null,
                        " ________________________________\n"
                        +"| Nombre del usuario: "+nomusu
			+"\n|--------------------------------|"
			+"\n| Dias: 2                         "
			+"\n|--------------------------------|"
			+"\n|Precio: $"+precios[1]
			+"\n| --------------------------------");                                  
                menu();
                }
		case 3 -> 
                {
                JOptionPane.showMessageDialog(null,
                        " ________________________________\n"
			+"| Nombre del usuario: "+nomusu
			+"\n|--------------------------------|"
			+"\n| Dias: 3                          "
                        +"\n|--------------------------------|"
			+"\n| Precio:$ "+precios[2]
			+"\n| --------------------------------");
                menu();
                }
		case 4 -> 
                {
                JOptionPane.showMessageDialog(null,
                        " ________________________________\n"
                        +" Nombre del usuario: "+nomusu
			+"\n|--------------------------------|"
			+"\n| Dias: 6                            "
			+"\n|--------------------------------|"
                        +"\n| Precio:$ "+precios[3]
			+"\n| --------------------------------");
                menu();
                
                }
                default ->{
                    JOptionPane.showMessageDialog(null,"Opcion incorrecta,se volvera a visualizar los turnos");
                    turno(); 
                
                }
                }
                }catch(NumberFormatException ex){
                    JOptionPane.showMessageDialog(null, "La opcion elegida es incorrecta,vuelva a ingresar un numero valido");
                    menu();
                }
                
	}

	public static void rut()  {
		int i;
		int j;
		String rutina[];
		
		// grupos musculares a trabajar
		// arreglo con rutina y dias de la semana
		rutina = new String[7];
		rutina[0] = "Pecho";
		rutina[1] = "Espalda";
		rutina[2] = "Pierna";
		rutina[3] = "Bicep";
		rutina[4] = "Tricep";
		rutina[5] = "Hombro";
		rutina[6] = "Abs";
                
		// de acuerdo al sexo de la persona,va a haber una matriz adecuada.  
		i = Integer.parseInt(JOptionPane.showInputDialog(   //Si no funciona poner i = 
                       "Seleccione su sexo\n"
                        +"1. Mujer\n"
                        +"2. Hombre"));
		// ciclo
		while (i>2) {
			i = Integer.parseInt(JOptionPane.showInputDialog("Usted eligió una opción incorrecta,vuelva a seleccionar su sexo"));
		}
		// funciones 
		// se elije la rutina con la cantidad de dias y ejercicios a hacer
                
		j = Integer.parseInt(JOptionPane.showInputDialog(
                        "Seleccione los dias a trabajar\n"
                       +"1. 1 dia a la semana\n"
                       +"2. 2 dias a la semana\n"
                       +"3. 3 dias a la semana\n"
                       +"4. 6 dias a la semana"));
               
		// ciclo
		while (j>4) {
			j = Integer.parseInt(JOptionPane.showInputDialog("Usted eligió una opción incorrecta,seleccione nuevamente su rutina"));
		}
		// condicionales
		// mujer y 1 dia a la semana
		if (i==1 && j==1) {           
                    
                        
			JOptionPane.showMessageDialog(null ,
                        "                            plan de ejercitacion de 1 dia\n"
			+"|  Lunes  |   Martes  |   Miercoles   |  Jueves   |  Viernes   |  Sabado   |  Domingo |\n"
			+"------------------------------------------------------------------------------------------------------------\n"
			+"|  nada    |   nada      |     "+rutina[2]+"        |   nada       |   nada      |   nada       | descanso |\n"
			+"|  nada    |   nada      |     "+rutina[6]+"             |   nada       |   nada      |   nada       | descanso |\n"
			+"|  nada    |   nada      |     "+rutina[1]+"     |   nada       |   nada       |   nada       | descanso |\n"
			+"------------------------------------------------------------------------------------------------------------\n"
			+"¿desea realizar otra operacion?");
			menu();
		} else {
			// mujer y 2 dias a la semana
			if (i==1 && j==2) {
				JOptionPane.showMessageDialog(null,
                                "                            plan de ejercitacion de 2 dias\n"
				+"|  Lunes  |   Martes  |   Miercoles   |  Jueves   |  Viernes   |  Sabado   |  Domingo |\n"
				+"------------------------------------------------------------------------------------------------------------\n"
				+"|   nada   |  "+rutina[2]+"    |     nada          |   "+rutina[3]+"     |    nada       |    nada      | descanso |\n"
				+"|   nada   |   "+rutina[6]+"        |     nada          |   "+rutina[2]+"    |    nada       |    nada      | descanso |\n"
				+"|   nada   |   "+rutina[1]+" |    nada          |   "+rutina[5]+"  |    nada       |    nada      | descanso |\n"
				+"------------------------------------------------------------------------------------------------------------\n"
				+"¿desea realizar otra operacion?");
				menu();
			} else {
				// mujer y 3 dias a la semana
				if (i==1 && j==3) {
					JOptionPane.showMessageDialog(null,                         
                                         "                            plan de ejercitacion de 3 dias\n"
					+"|  Lunes  |   Martes  |   Miercoles   |  Jueves   |  Viernes   |  Sabado   |  Domingo |\n"
					+"------------------------------------------------------------------------------------------------------------\n"
					+"|  "+rutina[2]+" |   nada       |     "+rutina[3]+"        |    nada      |  "+rutina[0]+"     |    nada      | descanso |\n"
					+"|   "+rutina[6]+"     |   nada       |    "+rutina[2]+"       |    nada       |  "+rutina[4]+"    |    nada      | descanso |\n"
					+"| "+rutina[1]+"|   nada       |   "+rutina[5]+"     |    nada       |  "+rutina[2]+"    |    nada      | descanso |\n"
					+"------------------------------------------------------------------------------------------------------------\n"
					+"¿desea realizar otra operacion?");
					menu();
				} else {
					// mujer y 6 dias a la semana
					if (i==1 && j==4) {
						JOptionPane.showMessageDialog(null,                     
                                                 "                             plan de ejercitacion de 6 dias\n"
						+"|  Lunes  |   Martes  |   Miercoles   |  Jueves   |  Viernes   |  Sabado   |  Domingo |\n"
						+"------------------------------------------------------------------------------------------------------------\n"
						+"|  "+rutina[2]+"  |     "+rutina[6]+"     |      "+rutina[0]+"       |     "+rutina[6]+"      |    "+rutina[0]+"    |a eleccion| descanso |\n"
						+"|    "+rutina[6]+"     |   "+rutina[3]+"    |      "+rutina[2]+"       |   "+rutina[4]+"   |   "+rutina[5]+"  |a eleccion| descanso |\n"
						+"| "+rutina[1]+" |   "+rutina[4]+"  |     "+rutina[5]+"     | "+rutina[1]+"  |    "+rutina[2]+"    |a eleccion| descanso |\n"
						+"------------------------------------------------------------------------------------------------------------\n"
						+"¿desea realizar otra operacion?");
						menu();
					} else {
						// hombre y 1 dia a la semana
						if (i==2 && j==1) {
							JOptionPane.showMessageDialog(null,
                                                         "                             plan de ejercitacion de 1 dia\n"
							+"|  Lunes  |   Martes  |   Miercoles   |  Jueves   |  Viernes   |  Sabado   |  Domingo |\n"
							+"------------------------------------------------------------------------------------------------------------\n"
							+"|  nada    |    nada     |      "+rutina[0]+"       |    nada     |     nada      |    nada     | descanso |\n"
							+"|  nada    |    nada     |       "+rutina[3]+"       |    nada     |     nada      |    nada     | descanso |\n"
							+"|  nada    |    nada     |       "+rutina[4]+"      |    nada     |     nada      |    nada     | descanso |\n"
							+"------------------------------------------------------------------------------------------------------------\n"
							+"¿desea realizar otra operacion?");
							menu();
						} else {
							// hombre y 2 dias a la semana
							if (i==2 && j==2) {
								JOptionPane.showMessageDialog(null,
                                                                 "                             plan de ejercitacion de 2 dias\n"
								+"|  Lunes  |   Martes  |   Miercoles   |  Jueves   |  Viernes   |  Sabado   |  Domingo |\n"
                                                                +"------------------------------------------------------------------------------------------------------------\n"         
								+"|   nada   |   "+rutina[0]+"   |        nada        |  "+rutina[1]+" |      nada     |     nada    | descanso |\n"
								+"|   nada   |   "+rutina[3]+"    |        nada        |   "+rutina[2]+"   |      nada     |     nada    | descanso |\n"
								+"|   nada   |   "+rutina[4]+"   |        nada        |  "+rutina[5]+"  |     nada     |     nada    | descanso |\n"
								+"------------------------------------------------------------------------------------------------------------\n"
								+"¿desea realizar otra operacion?");
								menu();
							} else {
								// hombre y 3 dias a la semana
								if (i==2 && j==3) {
									JOptionPane.showMessageDialog(null,
                                                                         "                             plan de ejercitacion de 3 dias\n"
									+"|  Lunes  |   Martes  |   Miercoles   |  Jueves   |  Viernes   |  Sabado   |  Domingo |\n"
									+"------------------------------------------------------------------------------------------------------------\n"
									+"| "+rutina[0]+"  |     nada    |     "+rutina[1]+"     |    nada      |      "+rutina[6]+"      |     nada     | descanso |\n"
									+"|  "+rutina[3]+"  |     nada    |       "+rutina[2]+"      |    nada      |    "+rutina[3]+"    |     nada     | descanso |\n"
									+"|  "+rutina[4]+" |     nada    |      "+rutina[5]+"    |    nada      |    "+rutina[0]+"   |     nada     | descanso |\n"
									+"------------------------------------------------------------------------------------------------------------\n"
									+"¿desea realizar otra operacion?");
									menu();
								} else {
									// hombre y 6 dias a la semana
									if (i==2 && j==4) {
										JOptionPane.showMessageDialog(null,
                                                                                 "                         plan de ejercitacion de 6 dias\n"
										+"|  Lunes  |   Martes  |   Miercoles   |  Jueves   |  Viernes   |  Sabado   |  Domingo |\n"
										+"------------------------------------------------------------------------------------------------------------\n"
										+"|  "+rutina[0]+"  |      "+rutina[6]+"     |      "+rutina[0]+"      |      "+rutina[6]+"     |    "+rutina[2]+"    |a eleccion| descanso |\n"
										+"|  "+rutina[3]+"   |    "+rutina[4]+"   |     "+rutina[2]+"      |    "+rutina[4]+"   |    "+rutina[3]+"     |a eleccion| descanso |\n"
										+"|  "+rutina[4]+"  |  "+rutina[1]+"  |    "+rutina[5]+"    |  "+rutina[1]+"  |    "+rutina[0]+"    |a eleccion| descanso |\n"
										+"------------------------------------------------------------------------------------------------------------\n"
										+"¿desea realizar otra operacion?");
										menu();
									}
								}
							}
						}
					}
				}
			}
		}
	}

	public static void cont()  {
            
                int nF = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de series a realizar"));
                int nC = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de repeticiones"));
                int matriz[][] = new int [nF][nC];
                //llenar matriz
                for (int i = 0; i < nF; i++) {
                    for (int j = 0; j < nC; j++) {
                        matriz[i][j] = Integer.parseInt(JOptionPane.showInputDialog("Numero de serie [" + (i + 1) +"] de la [" + (j + 1) + "] repeticion"));
                    }
                }
                //Imprimir la matriz
                String resultado = "";
                for (int i = 0; i < nF; i++) {
                    for (int j = 0; j < nC; j++) {                     
                        resultado += matriz[i][j];
                        resultado += "        ";
                    }
                    resultado += "\n";
                }
                JOptionPane.showMessageDialog(null, "Repeticiones realizadas\n"+resultado );	
         
		JOptionPane.showMessageDialog(null,"¿Desea realizar otra operacion?".toUpperCase());
		menu();
	}
}

        

