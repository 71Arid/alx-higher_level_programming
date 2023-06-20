#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2]);

let i = 0;
let j = 0;
const str = 'X';
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    let output = '';
    for (j = 0; j < x; j++) {
      output += str;
    }
    console.log(output);
  }
}
