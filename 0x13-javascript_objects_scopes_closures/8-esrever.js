#!/usr/bin/node
/* a function that returns the reversed version of a list */

exports.esrever = function (list) {
  let temp = '';
  let len = list.length;
  for (let i = 0; i < list.length / 2; i++) {
    temp = list[i];
    list[i] = list[len - 1];
    list[len - 1] = temp;
    len--;
  }
  return (list);
}
