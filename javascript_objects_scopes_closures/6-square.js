#!/usr/bin/node
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print();
  }
}

module.exports = Square;
