#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    const legend = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += legend;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
