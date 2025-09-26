#!/usr/bin/node
const firstArg = process.argv[2];

if (firstArg === undefined) {
  console.log(firstArg + ' is ' + firstArg);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
