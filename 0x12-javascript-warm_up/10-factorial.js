#!/usr/bin/node
function fact(a) {
  if (a === undefined) {
    return (1);
  }
  if (a === 0 || a === 1) {
    return (1);
  }
  return a * fact((a) - 1);
}
console.log(fact(parseInt(process.argv[2])));
