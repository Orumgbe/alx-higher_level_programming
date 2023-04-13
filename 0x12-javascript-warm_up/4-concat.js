#!/usr/bin/node

// Prints two arguments passed to it, format ... is ...
if (process.argv[2] && process.argv[3]) {
  let name = process.argv[2] + " is " + process.argv[3];
  console.log(name);
}
