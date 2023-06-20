#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2]);
let i = 0;

if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
