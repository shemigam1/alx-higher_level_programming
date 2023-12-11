#!/usr/bin/node
function fact(a) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}
console.log(fact(Number(process.argv[2])));
