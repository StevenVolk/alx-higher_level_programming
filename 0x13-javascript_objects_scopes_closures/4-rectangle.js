#!/usr/bin/node
//  a class Rectangle that defines a rectangle
// print() that prints the rectangle using the character X
// rotate() that exchanges the width and the height of the rectangle
// double() that multiples the width and the height of the rectangle by 2

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; ++i) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height =  temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
