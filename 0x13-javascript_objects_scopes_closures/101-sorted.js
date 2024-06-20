#!/usr/bin/node
const { dict } = require('./101-data.js');
const newOccurence = {};
for (const useridValue in dict) {
  const occurenceKey = dict[useridValue];
  if (!newOccurence[occurenceKey]) {
    newOccurence[occurenceKey] = [];
  }
  newOccurence[occurenceKey].push(useridValue);
}
console.log(newOccurence);
