#!/usr/bin/node

const num = Math.floor(process.argv[2]);
if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
