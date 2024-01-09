#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      for (let i = 0; i > this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    } else {
      for (let i = 0; i > this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
