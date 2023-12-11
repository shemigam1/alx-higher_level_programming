#!/usr/bin/env node
let size = Number(process.argv[2]);
if (size && size >= 0) {
	for (let i = 0; i < size; i++) {
		let line = "";
		for (let j = 0; j < size; j++) {
			line += 'X';
		}
		console.log(line);
	}
} else {
	console.log("Missing size");
}
