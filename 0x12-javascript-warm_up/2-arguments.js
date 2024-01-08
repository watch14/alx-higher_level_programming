#!/usr/bin/node

const x = process.argv.length - 2;

if (x === 0) {
  console.log("No argument");
} else {
  console.log("Arguments found");
}
