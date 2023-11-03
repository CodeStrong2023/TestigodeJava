
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Mega Tecnologia
 */
public class HolaMundo {

    public static void main(String[] args) {
        System.out.println("Hola mundo desde java");
        /*
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programacion";
        System.out.println(miVariableCadena);
         */

        //Var - inferencia de tipos en java
        /*
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        
        //soutv + tab
        //para ejecutar shift + f6
        //Ejercicio de Concatenacion
        var usuario = "Nicolas";
        var titulo = "Estudiante";
        var union = usuario + " " + titulo;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(a + b);
        System.out.println(usuario + a + b);
        System.out.println(usuario + (a + b));
         */
        //Caracteres Especiales
        /*
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre);//\n salto de linea
        System.out.println("Tabulacion: \t" + nombre);//\t espacio tabulado
        System.out.println("\t\t.:Menu:.");//Ejemplo \t
        System.out.println("Retroseso: \b" + nombre);//\b borra un espacio hacia atras
        System.out.println("Comillas Simples: \'"+ nombre +"\'");//\' comillas simples
        System.out.println("Comillas Dobles: \""+ nombre +"\"");//\" comillas dobles
         */
        //Clase Scanner
        /*
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();//nextLine: entrada del usuario
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("titulo2 = " + titulo2+" "+usuario2);
         */
        //Tipos numericos Enteros
        /*
        byte numEnteroByte = 10;
        System.out.println("Valor minimo del byte:"+ Byte.MIN_VALUE);//-128
        System.out.println("Valor maximo del byte:"+ Byte.MAX_VALUE);//127
        //Rangos minimos y maximos del numero Byte
        
        short numEnteroShort = 10;
        System.out.println("Valor minimo del short: "+ Short.MIN_VALUE);//-32768
        System.out.println("Valor maximo del short: "+ Short.MAX_VALUE);//32767
        
        int numEnteroInt = 10;
        System.out.println("Valor minimo del int: "+ Integer.MIN_VALUE);//-2147483648
        System.out.println("Valor maximo del int: "+ Integer.MAX_VALUE);//2147483647
        
        long numEnteroLong = 10;
        System.out.println("Valor minimo del long: "+ Long.MIN_VALUE);//-9223372036854775808
        System.out.println("Valor maximo del long: "+ Long.MAX_VALUE);//9223372036854775807
         */
        //Tipos Numericos Enteros
        /*
        float numFloat = 10.0F;//F de float, indica que la literal es de tipo flotante
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de float: " + Float.MIN_VALUE);//1.4E-45
        System.out.println("El valor maximo de Float: " + Float.MAX_VALUE);//3.4028235E38
        
        double numDouble = 10;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de Double: " + Double.MIN_VALUE);//4.9E-324
        System.out.println("El valor maximo de Double: " + Double.MAX_VALUE);//1.7976931348623157E308
         */
        //Inferencia de tipos "var" y tipos primitivos
        /*
        var numEntero = 20;//Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        
        var numFloat = 10.0;//Automaticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
         */
        //Tipos primitivos char
        /*
        char miVariableChar = 'a' ;
        System.out.println("miVariableChar = " + miVariableChar);
        char varCaracter = '\u0024';//Indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36;//Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';//Caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
         */
        //Tipos primitivos tipos booleanos
        /*
        boolean varBool = true;//a diferencia de python, true y false se escriben con minuscula
        
        System.out.println("varBool = " + varBool);
        
        if(varBool){       
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");          
        }
        
        //Algoritmo: ¿Es mayor de edad?
        
        var edad = 15; //Literal tiene presente la inferencia de tipos
        var adulto = edad >= 18; //exprecion booleana
        if(adulto){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }
         */
        //Conversion de tipos primitivos
        /*
        var edad = Integer.parseInt("20");//de tipo cadena a tipo entero
        System.out.println("edad= " + (edad + 1));//teniendo el numero entero se realiza la suma
        var valorPi = Double.parseDouble("3.14");//de tipo cadena a double
        System.out.println("Valor de Pi= " + valorPi);
        
        //Pedir valor (Scanner)
        
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad: ");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);
        
        //Convercion de tipo entero a string
        
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(3);
        System.out.println("fraseChar = " + fraseChar);
         */
        //Operadores en java
        /*
        int num1 = 5, num2 = 4;//no se puede con la inferencia de tipos(var)
        var solucion = num1 + num2;
        System.out.println("solucion de suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("Solucion de resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("Solucion de multiplicacion =" + solucion);
        
        solucion = num1 / num2;
        System.out.println("Solucion de divicion =" + solucion);
        
        var solucion2 = 3.4 /num2;
        System.out.println("Solucion 2 de divicion =" + solucion2);
        
        solucion = num1 % num2;//guarda residuo entero de la divicion
        System.out.println("Solucion residuo =" + solucion);
        
        if(num2 % 2 == 0)//no son necesaria las llaves si solo usamos una linea dentrod e cada bloque; una en if y otra en else
            System.out.println("Es un numero Par");
        else
            System.out.println("Es un numero Impar");
         */
        //Operadores de Asignacion
        /*
        int varNum1 = 1, varNum2 = 4;
        var varNum3 = varNum1 + 6 - varNum2;//una operacion//tambien se puede correr con una inferencia(var)
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1;// es igual que varNum1 + 1
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 -= 2;//resta
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;//multiplicacion
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4;//divicion
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6;//resto
        System.out.println("varNum1 = " + varNum1);
         */
        //Operadores Unarios : cambio de signo
        /*
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);
         */
        //Operador de Negacion
        /*
        var varC = true;
        var varD = !varC;//valor contrario = false
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
         */
        //Operadores Unarios de incremento: Preincremento
        /*
        var varE = 9;//va a dejar de ser 9
        var varF = ++varE;//se va a incrementar el valor//no solo se le asigna un valor a la variable F, sino que tambien va a cambiar el valor de la variable E
        System.out.println("varE = " + varE);
        System.out.println("varF = " + varF);
         */
        //Postincremento(simbolo despues de la variable)
        /*
        var varG = 3;//va a cambiar su valor
        var varH = varG++;//va a tomar el valor de la variable G antes del incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
         */
        //Operadores Unarios de decremento
        /*
        var varI = 4;
        var varJ = --varI;//El decremento afecta a ambas variables, como en el caso del preincremento
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);
         */
        //Postdecremento(simbolo despues de la variable)
        /*
        var varK = 8;
        var varL = varK--;//la variable K va a tener un decremento, en cambio la variable L va a tomar el valor de la variable K antes de decrementarse
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);
         */
        //Operadores de Igualdad
        /*
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);//son iguales?//nos va a arrojar si es verdadero o falso
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum;//son diferentes?
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);
        
        var fVar = cadenaA.equals(cadenaB);//se comparan las cadenas
        System.out.println("fVar = " + fVar);
         */
        //Operadores Relacionales
        /*
        var gVar = aNum >= bNum;// o <= != == >=
        System.out.println("gVar = " + gVar);
         */
        //Operadores Condicionales: and y or(&& y ||)
        /*
        var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;//rango del 0 al 10
        var respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        //en el caso del and, ambas afirmaciones deben ser verdaderas paar que sea true
        var vacaciones = true;
        var diaLibre = false;
        if(vacaciones || diaLibre)
            System.out.println("Papa puede asistir al juego de su hijo");
        else
            System.out.println("Papa no puede asistir al juego de su hijo");
        //en el caso del or, con que solo una de las afirmaciones sea verdadera, ya va a ser true
        */
        //Operador Ternario
        /*
        var resultadoT = (5 > 8) ? "Verdadero" : "Falso";//consta de tres partes
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);
        //se recomienda usarlo solo con expreciones sensillas//si es mas complejo se recomienda usar if / else
        */
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    }
}
