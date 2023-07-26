#!/usr/bin/node
const request = require('request');
let data;
const dict = {};
request(process.argv[2], function (_err, _res, body) {
  if (_err) {
    console.error(_err);
  } else {
    data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      const id = data[i].userId;
      const completed = data[i].completed;
      if (completed && !dict[id]) {
        dict[id] = 0;
      }

      if (completed) ++dict[id];
    }

    console.log(dict);
  }
});
