#!/usr/bin/env node
exports.callMeMoby = function visible (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
