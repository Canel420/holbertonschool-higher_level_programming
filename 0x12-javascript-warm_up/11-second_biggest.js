#!/usr/bin/node

const nums = process.argv.slice(2);
let big2 = 0;

if (nums.length > 1) {
  nums.sort();
  big2 = nums[nums.length - 2];
}

console.log(big2);
