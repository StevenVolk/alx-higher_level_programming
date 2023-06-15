#!/usr/bin/node

const array = process.argv;
let biggest = 0;
let big = 0;

for (let i = 0; i < array.length; i++) {
  let num = Number(array[i]);
  if (num > biggest) {
    big = biggest;
    biggest = num;
  } else if (num > big && num < biggest) {
    big = num;
  }
}
console.log(big);
