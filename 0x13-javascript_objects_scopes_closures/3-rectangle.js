#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || !w || !h) {
      return NaN;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    let i;
    for (i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
module.exports = Rectangle;
