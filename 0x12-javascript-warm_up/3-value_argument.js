#!/usr/bin/node

const args = process.argv;

let len = 0;
args.forEach((val, index) => {
  len++;
  if (index === 2) {
    console.log(val);
  }
});

if (len === 2) {
  console.log('No argument');
}
