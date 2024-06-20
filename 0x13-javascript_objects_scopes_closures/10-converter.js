#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    const digits = '0123456789ABCDEF';
    if (num === 0) {
      return '0';
    }
    let result = '';
    while (num > 0) {
      result = digits[num % base] + result;
      num = Math.floor(num / base);
    }
    return result;
  }
};
