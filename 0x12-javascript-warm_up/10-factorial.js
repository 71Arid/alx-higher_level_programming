#!/usr/bin/node
const args = process.argv;

function fact (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  }
  return a * fact(a - 1);
}

const answer = fact(Number(args[2]));
console.log(answer);
