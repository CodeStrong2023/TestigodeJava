
public class clase5 {
    public static void main(String[] args) {
        
        var numEntero = 20; //las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        
        var numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat);
        
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        
        //tipos primitivos char
        
        char miVariableChar = 'a';
        System.out.println("mivariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; //indicamos a Java la signacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
    }
}

