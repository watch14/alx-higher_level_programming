#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0 || n === 0 || n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

const x = parseInt(process.argv[2]);
const r = factorial(x);

console.log(r);
