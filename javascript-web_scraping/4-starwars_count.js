#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const film of results) {
      for (const character of film.characters) {
        if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
