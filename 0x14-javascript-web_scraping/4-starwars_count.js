#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present. */
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    let result = [];
    let charac = [];
    result = (JSON.parse(body).results);
    for (let i = 0; i < result.length; i++) {
      charac = result[i].characters;
      charac.forEach(element => {
        if (element.includes('18')) {
          count++;
        }
      });
    }
    console.log(count);
  }
});
