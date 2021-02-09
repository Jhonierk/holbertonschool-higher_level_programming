#!/usr/bin/node
const dict = require('./101-data').dict;
const data = {};
for (const i in dict) {
  if (data[dict[i]] === undefined) {
    data[dict[i]] = [];
  }
  data[dict[i]].push(i);
}
console.log(data);
