#!/usr/bin/node
/**
 * defines square that inherits from rectangle
 */
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
