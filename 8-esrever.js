#!/usr/bin/node
/* function that returns the reversed version of a list */

exports.esrever = function (list) {
  const newA = [];
  let i; let j = 0;
  for (i = list.length; i > 0; i--, j++) {
    newA[j] = list[i - 1];
  }
  return newA;
};
