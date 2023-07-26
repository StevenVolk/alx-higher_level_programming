#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (_err, _res, body) {
  if (!_err) {
    const chars = JSON.parse(body).characters;
    printMov(chars, 0);
  }
});

function printMov (chars, i) {
  request(chars[i], function (_err, _res, body) {
    if (!_err) {
      console.log(JSON.parse(body).name);
      if (i + 1 < chars.length) {
        printMov(chars, i + 1);
      }
    }
  });
}
