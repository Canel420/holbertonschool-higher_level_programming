#!/usr/bin/node

const axios = require('axios').default;
const id = process.argv[2];
let URL = 'https://swapi-api.hbtn.io/api/films/';
URL += id.toString() + '/';

axios.get(URL)
  .then(function (response) {
    console.log(response.data.title);
  });
