#!/usr/bin/node
/* Script that prints the title of a Star Wars movie */

const request = require('request');
const movieNumber = process.argv[2];
const movieEpisode = parseInt(movieNumber);
const url = `http://swapi-api.hbtn.io/api/films/${movieEpisode}`;

request(url, function (error, response, body) {
  if (error) {
    throw error;
  }
  console.log(JSON.parse(body).title);
});
