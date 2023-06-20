#!/usr/bin/node
const args = process.argv;
let i = 0;
let j = 0;

if (args.length <= 3) {
  console.log(0);
} else {
  for (i = 2; i < args.length; i++) {
    for (j = 2; j < args.length; j++) {
      if (parseInt(args[j]) < parseInt(args[j + 1])) {
        const temp = args[j];
        args[j] = args[j + 1];
        args[j + 1] = temp;
      }
    }
  }
  console.log(parseInt(args[3]));
}
