#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];

const string = process.argv[3];

if (!filepath || !string) {
  console.error('Usage: ./0-writefile.js <filepath> <string>');
  process.exit(1);
}

fs.writeFile(filepath, string, 'utf8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
