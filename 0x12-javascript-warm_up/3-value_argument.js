#!/usr/bin/node

const x = process.argv[2];

if (typeof x === 'undefined') {
  console.log('No argument');
} else {
  console.log(x);
}
