#!/usr/bin/node

const myVar = process.argv;
function factorialize (num) {
  if (num === 0) {
    return 1;
  } else {
    return (num * fatorialize(num - 1));
  }
}
if (myVar[2]) {
  console.log(factorialize(parseInt(myVar[2])));
} else if (!myVar[2]) {
  console.log(1);
}
