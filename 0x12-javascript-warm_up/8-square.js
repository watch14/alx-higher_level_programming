#!/usr/bin/node

const x = process.argv[2];

if (isNaN(x) || typeof x === 'undefined') {
  console.log('Missing size');
}
for (let i = 0; i < x; i++) {
  console.log('X'.repeat(x));
}
