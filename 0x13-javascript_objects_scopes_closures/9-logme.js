#!/usr/bin/node
/* prints the number of arguments already printed and the new argument value */

arguements = 0;
exports.logMe = function (item) {
  console.log(arguements + ': ' + item);
  arguements++;
}
