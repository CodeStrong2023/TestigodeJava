//Tipos datos Javascript
/* 
Aca se comenta adentro
*/


var nombre = "Ariel"; // Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
//Tipo numerico
var numero = 3000; //  Tipo numerico
console.log(numero);

var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "06545559977"
}
console.log(typeof objeto);

//Tipo de dato booleano
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion
function miFuncion() {}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);
//null: significa ausencia de valor
var y = null; //no es un dato pero su origen es objeto
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Citroen','Audi','BMW','Ford'];
console.log(typeof autos);
console.log(autos);

var z;
console.log(z);
console.log(typeof z);
