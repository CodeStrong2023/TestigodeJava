var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+' '+apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Betancud';
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee el num como str
console.log(juntos);
juntos = nombre + (78 + 17);//aqui se diferencia con parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //Concatenamos usando el operador simplificacion
console.log(nombre);

// Hoy ya no se usa var, se utiliza let y const 
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres"; una constante no se puede modificar
console.log(apellido2);

let x, y;   //Se pueden crear varias variables dentro de una misma linea
x = 17, y = 21; //Se puede hacer asignacion de varias variables dentro de la misma linea
let z = x + y;  //Se asigna el valor de la operacion
console.log(z)

let _1num = 31; //No utilizar numeros para iniciar el nombre
let rompiendo = "rompe";    //No utilizar palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);