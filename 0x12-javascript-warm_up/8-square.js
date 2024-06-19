#!/usr/bin/node
const sumA = parseInt(process.argv[2]);
const sumB = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

if (!isNaN(sumA) && !isNaN(sumB)) {
  const result = add(sumA, sumB);
  console.log(result);
} else {
  console.log('NaN');
}
