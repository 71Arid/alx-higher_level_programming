#!/usr/bin/node
/**
 * defines square that inherits from 5-square.js
 */
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        output += c;
      }
      console.log(output);
    }
  }
}

module.exports = Square;
