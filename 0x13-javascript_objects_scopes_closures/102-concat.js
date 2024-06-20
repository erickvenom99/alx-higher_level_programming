#!/usr/bin/node
const fs = require('fs');
if (process.argv.length !== 5) {
  console.error('Wrong input');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationFile = process.argv[4];

const file1Content = fs.readFileSync(file1Path, 'utf8');
const file2Content = fs.readFileSync(file2Path, 'utf8');

const result = `${file1Content}\n${file2Content}\n`;
fs.writeFileSync(destinationFile, result, 'utf8');
console.log('successful');
