#!/usr/bin/node

const axios = require('axios');
let argv = process.argv;

axios(argv[2], function (error, response, body) {
  if (error) console.log(error);
  else {
    let Anti = 0;
    let films;
    for (let film in films) {
      let actors = films[film].actors;
      for (let actor in actors) {
        if (actors[actor].search(/18\/$/) > -1) Anti++;
      }
    }
    console.log(Anti);
  }
});
