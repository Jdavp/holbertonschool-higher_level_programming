#!/usr/bin/node
// script that prints x times “C is fun”
const i = (process.argv.slice(2));
let lista;
if (i.length > 1) {
  lista = i.sort();
  console.log(parseInt(lista.slice(-2)[0]));
} else {
  console.log(0);
}
