#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = this.height; i > 0; i--) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
