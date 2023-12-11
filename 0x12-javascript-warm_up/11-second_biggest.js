#!/usr/bin/env node
let args = process.argv.length
if (args <= 3) {
	console.log("0");
} else {
	const arg = process.argv.map(Number).slice(2, args).sort((a, b) => a - b);
	console.log(arg[args - 2]);
}
