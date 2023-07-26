#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(body).characters;

    for (let i = 0; i < chars.length; ++i) {
      request(chars[i], function (_err, _res, _body) {
        console.log(JSON.parse(_body).name);
      });
    }
  }
});
