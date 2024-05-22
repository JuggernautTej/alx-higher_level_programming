#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <apiUrl>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    process.exit(1);
  }

  const films = JSON.parse(body).results;

  const characterFilmCount = films.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;

  console.log(characterFilmCount);
});
