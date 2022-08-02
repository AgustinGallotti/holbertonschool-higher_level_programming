#!/usr/bin/node

module.exports = class Rectangle {
  constructor (width, height) {
    this.width = width;
    this.height = height;
    if (height <= 0 || width <= 0) {
      new Object();
    }
  }
}
