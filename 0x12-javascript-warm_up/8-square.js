#!/usr/bin/node
/*
   script that prints a square
*/
const number = parseInt(process.argv[2]);
let i;
if (number) {
  for (i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
