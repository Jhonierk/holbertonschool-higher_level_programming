#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present. */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let element;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let result = [];
    result = (JSON.parse(body).characters);
    for (element of result) {
      request(element, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
