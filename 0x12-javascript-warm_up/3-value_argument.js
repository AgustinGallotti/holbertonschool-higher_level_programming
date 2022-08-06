#!/usr/bin/node

const f = process.argv;

if (f[2]) {
  console.log(f[2]);
} else {
  console.log('No argument');
}
