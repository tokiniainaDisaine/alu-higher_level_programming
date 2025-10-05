#!/usr/bin/node
const request = require('request');
request(process.argv[2], 'utf8', function (body) {
  console.log(body);
});
