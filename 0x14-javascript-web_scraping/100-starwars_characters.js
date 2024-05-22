#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

if (!id) {
  console.error('Usage: ./100-starwars_characters.js <id>');
  process.exit(1);
}

const swapi = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(swapi, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(charUrl => {
    request.get(charUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error(`Error: Status code ${charResponse.statusCode}`);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
