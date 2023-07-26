#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(`code: ${response.statusCode}`);
});
