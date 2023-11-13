#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, async function (error, response, body) {
  if (response.statusCode === 200) {
    const content = await JSON.parse(body).characters;
    for (const i in content) {
      const ans = await printer(content[i]);
      console.log(ans);
    }
  } else {
    console.log(error);
  }
});

async function printer (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (response.statusCode === 200) {
        const name = JSON.parse(body).name;
        resolve(name);
      } else {
        reject(error);
      }
    });
  });
}
