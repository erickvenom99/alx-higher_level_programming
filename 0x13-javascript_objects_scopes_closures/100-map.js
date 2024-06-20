#!/usr/bin/node
const { list } = require('./100-data.js');
const listNew = list.map((value, index) => value * index);
console.log(list);
console.log(listNew);
