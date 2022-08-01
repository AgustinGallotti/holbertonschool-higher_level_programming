#!/usr/bin/node
const p = 'process';
if (process.argv.length <= 2) {
  console.log('Not argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
