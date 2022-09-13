#!/usr/bin/node

const axios = require('axios').default;
const argv = process.argv
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2]

axios.get(url).then(function (response) {
  console.log(response.data.title);
});
