#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
//   console.error('error:', error);
  console.log(body["title"]);
});
