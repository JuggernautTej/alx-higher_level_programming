#!/usr/bin/node

const value = parseInt(process.argv[2]);
let index = 0;
if (!isNaN(value)) {
  while (index < value) {
    console.log('C is fun');
    index++;
  }
} else {
  console.log('Missing number of occurrences');
}
