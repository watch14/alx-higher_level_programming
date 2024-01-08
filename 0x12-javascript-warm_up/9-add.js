#!/usr/bin/node

const i = process.argv[2];
const y = process.argv[3];

if (typeof i === 'undefined' || typeof y === 'undefined') {
  console.log('NaN');
} else if (isNaN(i) || isNaN(y)) {
  console.log('NaN');
} else {
  const o = Number(i) + Number(y);
  console.log(o);
}
