#!/usr/bin/node
exports.esrever = function (list) {
  if (list.length === 0) {
    return [];
  }
  const reverseNewList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseNewList.push(list[i]);
  }
  return reverseNewList;
};
