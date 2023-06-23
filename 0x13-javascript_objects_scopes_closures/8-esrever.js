#!/usr/bin/node
exports.esrever = function (list) {
  const l = list.length;
  let j = 0;
  for (let i = l - 1; i >= 0; i--) {
    if (i > j) {
      const s = list[i];
      list[i] = list[j];
      list[j] = s;
    }
    j++;
  }
  return list;
};
