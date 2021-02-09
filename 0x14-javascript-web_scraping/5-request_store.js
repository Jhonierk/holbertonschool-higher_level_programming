#!/usr/bin/node
/*  script that gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fileR = require('fs');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fileR.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
