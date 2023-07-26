#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
let resJ;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    resJ = JSON.parse(body);
    console.log(resJ.title);
  }
});
