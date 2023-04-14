#!/usr/bin/node

// Searches for the second biggest integer in list of arguments
if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = [];

  for (let i = 2; i < process.argv.length; i++) {
    args[i - 2] = process.argv[i];
  }
  args.sort();
  console.log(args[args.length - 2]);
}
