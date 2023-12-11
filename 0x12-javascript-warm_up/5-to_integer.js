#!/usr/bin/env node
let number = Number(process.argv[3]);
if (number == 'NaN') {
	console.log("Not a number");
} else {
	console.log(`My number: ${number}`);
}
