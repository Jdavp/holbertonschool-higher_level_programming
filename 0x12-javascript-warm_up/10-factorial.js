#!/usr/bin/node
// script that prints x times “C is fun”
function factorial (n) {
  if (isNaN(parseInt(n)) || parseInt(n) === 0 || parseInt(n) === 1) {
    return (1);
  } else {
    return (parseInt(n) * factorial(parseInt(n) - 1));
  }
}
console.log(factorial(process.argv[2]));
