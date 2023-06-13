#!/usr/bin/node
exports add = function (a, b) {
  console.log(Number(a) + Number(b));
}
add(process.argv[2], process.argv[3]);
