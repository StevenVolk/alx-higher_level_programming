#!/usr/bin/node

/* prints a message depending of the number of arguments passed */
let len = process.argv.length;
if (len === 2) {
	console.log('No argument');
} else if (len === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
