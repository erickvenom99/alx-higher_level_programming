#!/usr/bin/node
/* that computes the number of tasks completed by user id. */

const request = require('request');

const Url = 'https://jsonplaceholder.typicode.com/todos';

request(Url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 0;
        }
        completedTasksByUser[todo.userId]++;
      }
    });

    Object.keys(completedTasksByUser).forEach(userId => {
      console.log(`User ${userId} has completed ${completedTasksByUser[userId]} tasks.`);
    });
  } else {
    console.error('Error fetching data:', error);
  }
});
