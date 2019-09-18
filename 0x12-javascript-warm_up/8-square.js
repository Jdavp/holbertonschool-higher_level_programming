#!/usr/bin/node
// script that prints x times “C is fun”
const i = process.argv[2];
let x; let y; let z = '';

if (i) {
  for (x = 0; x < i; x++) {
    z = '';
    for (y = 0; y < i; y++) {
      z += 'X';
    }
    console.log(z);
  }
} else {
  console.log('Missing size');
}
