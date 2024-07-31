#!/usr/bin/env node

/* script that prints the number of movies */
let count = 0;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function (error, response, body) {
  if (error) throw error;

  let film, character;
  for (film of JSON.parse(body).results) {
    for (character of film.characters) {
      if (character.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
