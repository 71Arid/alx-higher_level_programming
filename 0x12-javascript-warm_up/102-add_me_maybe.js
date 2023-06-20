#!/usr/bin/node
let b = 1;
exports.addMeMaybe = function (a, c) {
  b += a;
  c(b);
};
