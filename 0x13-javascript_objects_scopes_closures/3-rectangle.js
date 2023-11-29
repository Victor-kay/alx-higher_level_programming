#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      Object.create(null);
    }
  }

  print() {
    // Check if width and height are defined before printing
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let s = '';
        for (let j = 0; j < this.width; j++) {
          s += 'X';
        }
        console.log(s);
      }
    }
  }
}

module.exports = Rectangle;
