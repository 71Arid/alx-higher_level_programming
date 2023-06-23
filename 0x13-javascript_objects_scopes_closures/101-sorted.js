#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dict2 = { };
for (const id in dict) {
  const occ = dict[id];
  if (dict2[occ]) {
    dict2[occ].push(id);
  } else {
    dict2[occ] = [id];
  }
}
console.log(dict2);
