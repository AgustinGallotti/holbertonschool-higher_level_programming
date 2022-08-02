#!/usr/bin/node

const p = process.argv;
const one = 'C is fun\n';
const two = 'Python is cool\n';
const three = 'JavaScript is amazing';

while (one && two && three) {
  console.log(one + two + three);
  break;
}
