/*
JavaScript script that fetches the character name from this 
URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
*/
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (query) {
    query.results.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
});