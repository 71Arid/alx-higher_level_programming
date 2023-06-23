#!/usr/bin/node
const list = require('./100-data.js').list;
const list1 = list.map((x, i) => {
  return x * i;
});
console.log(list);
console.log(list1);
