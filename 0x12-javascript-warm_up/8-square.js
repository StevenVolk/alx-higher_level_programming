#!/usr/bin/node

const size = Number(process.argv[2]);

for (let i = 0; i < size; ++i){
	let text = ''
	for (let j = 0; j < size; ++j){
		text += 'X';
	}
	console.log(text);
}
if (!size){
	console.log('Missing size');
}
