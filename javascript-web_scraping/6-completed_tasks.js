#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  const result = {};
  for (const task of JSON.parse(body)) {
    result[task["userId"]] = 0;
    if (task.completed === true) {
      result[task["userId"]]++;
    }
  }
  console.log(result);
});
