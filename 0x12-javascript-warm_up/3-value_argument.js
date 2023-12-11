#!/usr/bin/node
let args = process.argv.length
if (args < 3) {
  console.log('No argument');
} else {
    for (let i = 2; i < args; i++) {
      console.log(process.argv[i]);
    }
}
