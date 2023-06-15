#!/usr/bin/node
/*  a script that imports an array and computes a new array */

const list = require('./100-data').list;
console.log(list);
let cloneList = [...list];
for (let i = 0; i < list.length; ++i) {
  cloneList[i] = cloneList[i] * i;
}
console.log(cloneList);
