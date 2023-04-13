#!/usr/bin/node

// Prints text on screen
const myArg = process.argv[2];

if (isNaN(Number(myArg))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArg);
}
