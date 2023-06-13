#!/usr/bin/node

const array = process.argv;
let biggest = 0;
let big = 0;

for (let i = 0; i < array.length; ++i) {
 if (array[i] > biggest) {
  big = biggest;
  biggest = array[i];
 } else if (array[i] > big && array[i] < biggest) {
  big = array[i];
 }
}

console.log(big);
