#!/usr/bin/node

const request = require('request');

const url = (process.argv[2]);
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let occurrances = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.includes('https://swapi.co/api/people/18/')) {
        occurrances++;
      }
    }
    console.log(occurrances);
  }
});
