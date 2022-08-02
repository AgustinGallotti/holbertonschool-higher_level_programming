#!/usr/bin/node

const p = process.argv;

if (parseInt(p[2])) {
  console.log("My number: " + parseInt(p[2]));
} else {
  console.log("My number: " + "Not a number");
}
