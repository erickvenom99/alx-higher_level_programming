#!/usr/bin/node
/* that computes the number of tasks completed by user id. */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;
  const users = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});
