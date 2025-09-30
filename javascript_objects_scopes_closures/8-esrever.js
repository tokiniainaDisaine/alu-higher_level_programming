#!/usr/bin/node
exports.esrever = function (list) {
  let reverse = [];
  for (let i = list.length; i > 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
