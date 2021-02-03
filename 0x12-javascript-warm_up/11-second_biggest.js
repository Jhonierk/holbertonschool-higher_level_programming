#!/usr/bin/node
/*
  script that searches the second biggest integer in the list of arguments.
*/
const argv = process.argv;
const numberArgv = argv.length;

if (numberArgv <= 3) {
  console.log('0');
} else {
  const secondb = argv.sort(function (a, b) { return (b - a); });
  console.log(secondb[3]);
}
