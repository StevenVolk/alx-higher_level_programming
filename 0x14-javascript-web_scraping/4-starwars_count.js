#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let num_of_movies = 0;
request(url, function (_err, _res, body) {
  body = JSON.parse(body).results;
  for (let i = 0; i < body.length; i++) {
    const chars = body[i].characters;
    for (let j = 0; j < chars.length; j++) {
      const c = chars[j];
      const charId = c.split('/')[5];
      if (charId === '18') {
        num_of_movies += 1;
      }
    }
  }
  console.log(num_of_movies);
});
