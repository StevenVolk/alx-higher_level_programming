#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

let myObj = myObject;
myObj["value"] = 89;
console.log(myObject);
