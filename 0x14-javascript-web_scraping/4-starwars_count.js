#!/usr/bin/node
/* prints the number of movies where the character “Wedge Antilles” is present */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieDetails = JSON.parse(body).results;
    const wedgeMovies = movieDetails.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(`Number of movies with Wedge Antilles (character ID ${characterId}): ${wedgeMovies.length}`);
  } else {
    console.error('Error fetching data from the API:', error);
  }
});
