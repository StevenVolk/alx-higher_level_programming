#!/usr/bin/node

num = Number(process.argv[2]);
if (num) {
	console.log("Number: " + num);
} else {
	console.log('Not a number');
}
