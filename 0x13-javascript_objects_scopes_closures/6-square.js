#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let iter = 0; iter < this.height; iter++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
