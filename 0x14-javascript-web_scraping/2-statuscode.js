#!/usr/bin/node

const request = require('request');

const theUrl = process.argv[2];

if (!theUrl) {
  console.error('Usage: ./2-statuscode.js <theUrl>');
  process.exit(1);
}

request.get(theUrl, (error, response) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else {
    console.log('code:', response.statusCode);
  }
});
