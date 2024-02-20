#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const film = JSON.parse(body).results;

    const count = film.reduce((total, film) => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        return total + 1;
      }
      return total;
    }, 0);

    console.log(count);
  }
});
