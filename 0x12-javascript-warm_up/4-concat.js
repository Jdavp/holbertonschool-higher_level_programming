#!/usr/bin/node
// script that prints the first argument passed to it
if (process.argv[1] && process.argv[2]) {
  console.log('undefined is undefined');
} else if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2] + process.arvg[3]);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
