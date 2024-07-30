#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file. */

const fs = require('fs');
const request = require('request');
const [, , url, filePath] = process.argv;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(filePath, body, { encoding: 'utf-8' });
    console.log(`Content saved to file: ${filePath}`);
  } else {
    console.error('Error fetching data from the URL:', error);
  }
});
