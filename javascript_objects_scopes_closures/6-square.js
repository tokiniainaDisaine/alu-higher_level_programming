#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    super.print();
  }
}

module.exports = Square;
