//Tipos datos Javascript
/* 
Aca se comenta adentro
*/


var nombre = "Ariel"; // Tipo Str
console.log(nombre);

var numero = 3000; //  Tipo numerico

var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2143435135"
}
console.log(typeof objeto);

// Tipo de datos boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion
function miFuncion() {}
console.log(miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

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

//Null: significa ausencia de valor
var y = null; //null no es tipo de dato pero es de tipo objet
console.log(typeof y);

//Tipo de dato array y empty string
var autos = ["Citroen","Audi","BMW","Ford"];
console.log(typeof autos);

var z = '';
console.log(z); //Esto se refiere a una cadena vacia
console.log(typeof z);