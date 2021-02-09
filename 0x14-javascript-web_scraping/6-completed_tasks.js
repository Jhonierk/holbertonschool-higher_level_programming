#!/usr/bin/node
/* script that computes the number of tasks completed by user id. */
const request = require('request');
const dict = {};
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const info = JSON.parse(body);
    let elemt;
    for (elemt of info) {
      if (elemt.completed) {
        if (elemt.userId in dict) {
          dict[elemt.userId] += 1;
        } else {
          dict[elemt.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
}
);
