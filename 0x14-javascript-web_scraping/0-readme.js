#!/usr/bin/node

const fs = require('fs');
const doc = process.argv[2];

fs.readFile(doc, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
