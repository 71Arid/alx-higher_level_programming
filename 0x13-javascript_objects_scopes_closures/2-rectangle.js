#!/usr/bin/node
/**
 * defines a rectangle
 */
class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
