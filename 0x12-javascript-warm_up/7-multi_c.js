#!/usr/bin/node

/* prints x times “C is fun */
const times = process.argv[2];

for (let i = 0; i < times; ++i) {
  console.log('C is fun');
}

if (!times) {
  console.log('Missing number of occurrences');
}
