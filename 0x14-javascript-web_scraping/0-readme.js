#!/usr/bin/node
/* A script that prints the content of a file */

const fs = require('fs');
const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
