#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w / h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let iter = 1; iter <= this.height; iter++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
