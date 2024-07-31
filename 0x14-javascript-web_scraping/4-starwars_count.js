#!/usr/bin/node
/* script that prints the number of movies */
let count = 0;
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;

  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
