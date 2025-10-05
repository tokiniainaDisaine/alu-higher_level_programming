#!/usr/bin/node
const request = require('request');
request('https://jsonplaceholder.typicode.com/todos', function (body) {
  var result = {};
  for (const task of body) {
    result[task[userId]] = 0;
  }

  for (const task of body) {
    if (task["completed"] === true) {
        result[task[userId]]++; 
    }
  }
  return result;
});
