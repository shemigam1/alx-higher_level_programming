#!/usr/bin/node
let number = Number(process.argv[3]);
if (!number) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
