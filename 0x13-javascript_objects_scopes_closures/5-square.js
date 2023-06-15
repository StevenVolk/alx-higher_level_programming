#!/usr/bin/node
// class notation for defining your class and extends
// must take 1 argument: size
// The constructor of Rectangle must be called (by using super())
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
