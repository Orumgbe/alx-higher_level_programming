#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const users = {};

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  const bodyObj = JSON.parse(body);

  for (let i = 0; i < bodyObj.length; i++) {
    const tmp = bodyObj[i].userId;
    if (bodyObj[i].completed) {
      users[tmp] = (users[tmp] || 0) + 1;
    }
  }
  console.log(users);
});
