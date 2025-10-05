#!/usr/bin/node
const request = require('request');
request('https://jsonplaceholder.typicode.com/todos', function (error, response, body) {
  const result = {};
  for (const task of JSON.parse(body)) {
    result[task["userId"]] = 0;
    if (task.completed === true) {
      result[task["userId"]]++;
    }
  }
  return result;
});
