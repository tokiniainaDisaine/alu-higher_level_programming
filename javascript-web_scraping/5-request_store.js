#!/usr/bin/node
const request = require('request');
request(process.argv[2], 'utf8', function (error, response, body) {
  if (error) {
    console.error(`Error fetching URL: ${error}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(`Error writing file: ${err}`);
      }
    });
  }
});
