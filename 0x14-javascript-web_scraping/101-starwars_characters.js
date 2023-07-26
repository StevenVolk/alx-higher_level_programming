#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, function (err, res, body) {
  if (!err) {
    let chars = JSON.parse(body).characters;
    printMov(chars, 0);
  }
});

function printMov(chars, i) {
  request(chars[0], function (_err, _res, _body) {
    if (!_err) {
      console.log(JSON.parse(_body).name);
      if (index + 1 < chars.length) {
        printMov(chars, i + 1);
      }
    }
  });
}
