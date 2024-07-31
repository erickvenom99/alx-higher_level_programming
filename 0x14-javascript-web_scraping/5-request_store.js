#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file. */

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) throw error;
  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) throw err;
  });
});
