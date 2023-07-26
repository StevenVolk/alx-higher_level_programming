#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let numOfMovies = 0;
let data;

request(url, function (_err, _res, body) {
  data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    const chars = data[i].characters;
    for (let j = 0; j < chars.length; j++) {
      const ch = chars[j];
      const charId = ch.split('/')[5];
      if (charId === '18') {
        numOfMovies += 1;
      }
    }
  }
  console.log(numOfMovies);
});
