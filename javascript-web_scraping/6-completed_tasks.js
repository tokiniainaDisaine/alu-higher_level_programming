#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const result = {};
    for (const task of JSON.parse(body)) {
      if (task.completed && result[task.userId] === undefined) {
        result[task.userId] = 1;
      } else if (task.completed) {
        result[task.userId] += 1;
      }
    }
    console.log(result);
  }
});
