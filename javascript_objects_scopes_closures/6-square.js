#!/usr/bin/node
class Square extends Rectangle {
    constructor(size) {
        this.size = size;
    }

    charPrint(c="X") {
        for (let i = 0; i < this.size; i++) {
            console.log(c.repeat(this.size));
        }
    }
}

module.exports = Square;
