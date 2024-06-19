#!/usr/bin/node
const argCount = process.argv[2];
const x = parseInt(argCount);
let i = 0;
if (!isNaN(x)) {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
