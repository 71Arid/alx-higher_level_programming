#!/usr/bin/node
let i = 0;
exports.callMeMoby = function (a, c) {
  for (i = 0; i < a; i++) {
    c();
  }
};
