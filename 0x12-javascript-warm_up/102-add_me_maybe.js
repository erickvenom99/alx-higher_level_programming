#!/usr/bin/env node
exports.addMeMaybe = function (number, theFunction) {
  const incrementNumber = number + 1;
  theFunction(incrementNumber);
};
