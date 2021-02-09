#!/usr/bin/node
/*  class Square that defines a square and inherits from Square of 5-square.js */
class Square extends require('./5-square') {
  charPrint (c) {
    let i;
    for (i = 0; i < this.height; i++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
