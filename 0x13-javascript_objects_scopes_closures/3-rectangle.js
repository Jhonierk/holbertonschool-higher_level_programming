#!/usr/bin/node
/* Create an instance method called print() that prints the rectangle using the character X */
class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0 || h === undefined || w === undefined) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
