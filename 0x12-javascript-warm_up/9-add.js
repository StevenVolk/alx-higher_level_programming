#!/usr/bin/node
function add(a, b) {
	let c = Number(a) + Number(b);
	console.log(c);
}
add (process.argv[2], process.argv[3]);
