//Tipos de datos en Javascript

//tipo string
var nombre = "Ariel";
console.log(nombre);//utilizamos typeof para reconocer el tipo de variable en la consola
nombre = 7;
console.log(nombre);
nombre = 12.3;
console.log(nombre);

//tipo numerico
var numero = 3000;
console.log(numero);

//tipo objeto
var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2625578923"
}
console.log(objeto);

//tipo de dato booleano
var bandera = true;
console.log(bandera);

//tipo de dato funcion
function miFuncion(){}
console.log(miFuncion);

//tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//tipo de dato undefined
var x;
console.log(x);
//null: significa ausencia de valor
var y = null;//null no es un tipo de dato, pero su origen es object
console.log(y);

//tipo de dato array y empty string
//un arreglo es de tipo object
var autos = ["Citroen","Audi","BMW"];
console.log(autos);
var z = "";
console.log(z);
//cadena vacia




