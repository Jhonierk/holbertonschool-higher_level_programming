#!/usr/bin/node
/*
    If w or h is equal to 0 or not a positive integer, create an empty object
*/
class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0 || h === undefined || w === undefined) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
