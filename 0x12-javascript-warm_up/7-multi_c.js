#!/usr/bin/node
// script that prints x times “C is fun”
let i = process.argv[2];
if (i) {
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
} else {
  console.log('Missing number of occurrences');
}
