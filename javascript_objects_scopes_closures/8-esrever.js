#!/usr/bin/node
exports.esrever = function (list) {
  let occurence = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] == searchElement) {
      occurence++;
    }
  }
  return occurence;
};
