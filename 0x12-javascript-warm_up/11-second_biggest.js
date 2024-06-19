#!/usr/bin/env node
const argNum = process.argv.slice(2);
if (argNum.length < 2) {
  console.log('0');
} else {
  let secondBiggest = 0;
  let largest = 0;
  for (const num of argNum) {
    const numInt = Number(num);
    if (numInt > largest) {
      secondBiggest = largest;
      largest = numInt;
    } else if (numInt > secondBiggest && numInt !== largest) {
      secondBiggest = numInt;
    }
  }
  console.log(secondBiggest);
}
