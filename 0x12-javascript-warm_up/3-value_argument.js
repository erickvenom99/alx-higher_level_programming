#!/usr/bin/node
const message = process.argv[2];
if (message) {
  console.log(message);
} else {
  console.log('No Argument');
}
