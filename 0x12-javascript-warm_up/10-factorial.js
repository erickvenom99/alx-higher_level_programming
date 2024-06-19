#!/usr/bin/env node
const [, , num] = process.argv;

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (!isNaN(Number(num))) {
  const result = factorial(num);
  console.log(result);
} else {
  console.log(1);
}
