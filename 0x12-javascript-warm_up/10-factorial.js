#!/usr/bin/node
const [, , n] = process.argv;
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (!isNaN(Number(n))) {
  const result = factorial(n);
  console.log(result);
} else {
  console.log(1);
}
