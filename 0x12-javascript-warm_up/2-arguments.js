#!/usr/bin/node
/*
    script that prints a message depending of the number of arguments passed
*/
const argv = process.argv;
const numberArgv = argv.length;
if (numberArgv === 2) {
  console.log('No argument');
} else if (numberArgv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
