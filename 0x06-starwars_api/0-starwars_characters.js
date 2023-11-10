#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, function (error, response, body) {
  if (response.statusCode === 200) {
    const content = JSON.parse(body).characters;
    content.forEach((value, index, array) => {
      request(value, (error, response, body) => {
        if (response.statusCode === 200) {
          const name = JSON.parse(body).name;
          console.log(name);
        } else {
          console.log(error);
        }
      });
    });
  } else {
    console.log(error);
  }
});
