#!/usr/bin/node

const num = process.argv[2];

function factorial (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else if (a < 0) {
    return -1;
  } else {
    return (a * factorial(a - 1));
  }
}

console.log(factorial(num));
