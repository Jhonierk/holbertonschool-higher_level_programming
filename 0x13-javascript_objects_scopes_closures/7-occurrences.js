#!/usr/bin/node
/*  function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let elem = '';
  for (elem of list) {
    if (elem === searchElement) {
      count++;
    }
  }
  return count;
};
