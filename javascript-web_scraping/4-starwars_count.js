#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/', function (error, response, body) {
  let count;
  for (const film of body.results) {
    for (const character of film.characters) {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
  }
  return count;
});
