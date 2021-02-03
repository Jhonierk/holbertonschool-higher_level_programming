#!/usr/bin/node
/*
   script that computes and prints a factorial
*/

function factorial (n) {
  if (!n) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
const numFac = parseInt(process.argv[2]);
const fac = factorial(numFac);
console.log(fac);
