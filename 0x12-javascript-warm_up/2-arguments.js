#!/usr/bin/node

const p = process.argv;

if (p.length <= 2) {
  console.log('No argument');
} else if (p.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
