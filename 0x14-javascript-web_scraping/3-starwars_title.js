#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

if (!id) {
  console.error('Usage: ./3-starwars_title.js <id>');
  process.exit(1);
}

const swapi = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(swapi, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    process.exit(1);
  }

  const film = JSON.parse(body);
  console.log(film.title);
});
