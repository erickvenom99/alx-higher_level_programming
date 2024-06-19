#!/usr/bin/env node

const message = process.argv.length - 2;
if (message === 0) {
  console.log('No argument');
} else if (message === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
