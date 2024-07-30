#!/usr/bin/node
/* Script that prints the title of a Star Wars movie */

const request = require('request');
const movieNumber = process.argv[2];
const movieEpisode = parseInt(movieNumber);
const url = `https://swapi-api.alx-tools.com/api/films/${movieEpisode}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movieDetails = JSON.parse(body);
  const movieTitle = movieDetails.title;
  console.log(`Title: ${movieTitle}`);
});
