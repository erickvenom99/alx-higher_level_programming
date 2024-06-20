#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let rectangle = '';
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += 'X';
        }
        rectangle += line + '\n';
      }
      console.log(rectangle.trim());
    } else {
      console.log('Cannot print an empty rectangle.');
    }
  }
}
module.exports = Rectangle;
