#!/usr/bin/node
let args = process.argv.length;
if (args < 3) {
  console.log('No arguments');
} else if (args == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
