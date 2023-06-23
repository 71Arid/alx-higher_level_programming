#!/usr/bin/node
const args = process.argv;
const fs = require('fs');

const a = fs.readFileSync(args[2], 'utf8');
const b = fs.readFileSync(args[3], 'utf8');
const c = a + b;

fs.writeFileSync(args[4], c);
const out = fs.readFileSync(args[4], 'utf8');
console.log(out);
