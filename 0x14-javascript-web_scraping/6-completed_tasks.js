#!/usr/bin/node

const request = require('request');

const url = (process.argv[2]);
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let task_completed = 0;
    const id = JSON.parse(body).id;
    for (let i = 0; i < results.length; i++) {
      if (results[i].includes('true')) {
        occurrances++;
      }
	console.log(id:occurrances,);
    }
  }
});
