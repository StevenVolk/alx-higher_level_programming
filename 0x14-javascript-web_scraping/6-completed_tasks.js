#!/usr/bin/node

const request = require('request');
let data;
const dict = {};

request(process.argv[2], function (_err, _res, body) {
  if (_err) {
    console.error(_err);
  } else {
    data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const id = result.userId;
        if (!(id in dict)) {
          dict[id] = 0;
	}
        dict[id] += 1;
      }
    });
    console.log(dict);
  }
});
