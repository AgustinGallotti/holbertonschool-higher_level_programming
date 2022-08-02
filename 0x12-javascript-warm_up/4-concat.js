#!/usr/bin/node

const p = process.argv;

if (p[2] && p[3]) {
  console.log(p[2] + " is " + p[3]);
} else if (p[2]) {
  console.log(p[2] + " is " + "undefined")
}
else {
  console.log("undefined" + " is " + "undefined");
}
