#!/usr/bin/node
const args = process.argv;
let i = 0;
while (args[i]) {
  i = i + 1;
}

if (i === 2) { console.log('No Argument'); } else { console.log(args[2]); }
