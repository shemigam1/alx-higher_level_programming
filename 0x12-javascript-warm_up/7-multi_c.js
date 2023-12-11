#!/usr/bin/node
const power = parseInt(process.argv[2]);
if (power) {
  for (let i = 0; i < power; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
