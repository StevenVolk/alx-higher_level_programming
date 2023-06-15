#!/usr/bin/node
// class notation for defining your class and extends
// must take 1 argument: size
// The constructor of Rectangle must be called (by using super())
const tempSquare = require('./5-square');

module.exports = class Square extends tempSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; ++i) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
};
