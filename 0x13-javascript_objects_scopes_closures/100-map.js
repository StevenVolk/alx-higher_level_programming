#!/usr/bin/node
/*  a script that imports an array and computes a new array */

const list = require('./100-data').list;
console.log(list);
const cloneList = list.map((num, index) => num * index);
console.log(cloneList);
