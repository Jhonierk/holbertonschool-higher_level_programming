#!/usr/bin/node
/* script that display the status code of a GET request. */
const request = require('request');
request(process.argv[2], function (err, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + body.statusCode);
  }
});
