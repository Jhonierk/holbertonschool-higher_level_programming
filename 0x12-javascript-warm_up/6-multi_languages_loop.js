#!/usr/bin/node
/*
   script that prints 3 lines but by using an array of string and a loop
*/
const lines = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let message;
for (message of lines) {
  console.log(message);
}
