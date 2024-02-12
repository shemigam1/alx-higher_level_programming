#!/usr/bin/node
const args = process.argv.length;
if (args <= 3) {
  console.log(0);
} else {
  const arg = process.argv.slice(2).map(Number);
  const sorted = arg.sort(function(a, b){return b - a});
  console.log(sorted[1]);
}
