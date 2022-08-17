#!/usr/bin/node

const dict = require('./101-data').dict;
const dict2 = {};

for (const element in dict) {
  if (!dict2[dict[element]]) {
    dict2[dict[element]] = [];
  }
  dict2[dict[element]].push(element);
}

console.log(dict2);
