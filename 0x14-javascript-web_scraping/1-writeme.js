#!/usr/bin/node
/* script that writes a string to a file. */
const fileR = require('fs');
fileR.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
