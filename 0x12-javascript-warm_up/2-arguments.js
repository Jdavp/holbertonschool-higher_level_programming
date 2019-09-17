#!/usr/bin/node
// prints a message depending of the number of arguments passed
if (process.argv.length > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
