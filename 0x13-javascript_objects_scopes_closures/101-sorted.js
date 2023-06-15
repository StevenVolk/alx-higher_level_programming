#!/usr/bin/node
/* a script that imports a dictionary of occurrences by user id and */
/* computes a dictionary of user ids by occurrence */

const dict = require('./101-data').dict;
const newDict = {};
for (let key in dict) {
  let value = dict[key];
  if (value in newDict) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}
console.log(newDict);
